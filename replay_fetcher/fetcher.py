import datetime
import typing
import pychasing
import asyncio
import concurrent.futures
from . import models
import random
import mysql.connector
from dotenv import load_dotenv
import os

def db_connect():
    try:
        load_dotenv()
        db_pass = os.getenv("DBPASS")
        db = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password = db_pass
            )
        cursor = db.cursor()
    except mysql.connector.Error as error:
            print('Access Denied - Invalid Username or Password')
    else:
        try:
            cursor.execute("USE replaydata;")
        except mysql.connector.Error:
            print('Database does not exist...')
        finally:
            cursor.execute("SELECT DATABASE();")
            print("Successfully connected to database: ", cursor.fetchone()[0])
    return db, cursor


def fetch(client: pychasing.Client, replay_id: str) -> models.Replay:
    res = client.get_replay(replay_id, print_error=True)
    if res.status_code != 200:
        return
    return models.Replay(res.json())

def replays_list_cleaner(mini_replays: list[dict]) -> list[str]:
    id_list = []
    for r in mini_replays:
        if r["duration"] > 100:
            try:
                id_list.append(r["id"])
            except Exception:
                pass
    return id_list

async def fetch_many(executer, client: pychasing.Client,
                     replay_ids: list[str]):
    loop = asyncio.get_event_loop()
    waits: list = []
    for id in replay_ids:
        waits.append(loop.run_in_executor(executer, fetch, client, id))
    return await asyncio.wait(waits, return_when=asyncio.ALL_COMPLETED)


async def start(dump_replays: typing.Callable[[list[models.Replay]], None],
                client: pychasing.Client, replay_batch_size: int,
                max_workers: int) -> None:
    executer = concurrent.futures.ThreadPoolExecutor(max_workers=max_workers)
    rank_ranges = [
    ("bronze-1", "bronze-3"),
    ("silver-1", "silver-3"),
    ("silver-1", "silver-3"),
    ("gold-1", "gold-3"),
    ("platinum-1", "platinum-3"),
    ("diamond-1", "diamond-3"),    
    ("champion-1", "champion-3"),
    ("grand-champion-1", "grand-champion-1"),
    ("grand-champion-2", "grand-champion-2"),
    ("grand-champion-3", "grand-champion-3"),  
    ("supersonic-legend", "supersonic-legend")
]
    playlists = ["ranked-duels", "ranked-doubles", "ranked-standard"]
    db, cursor = db_connect()
    start_date = datetime.datetime(2020, 9, 23, 0, 0, 0)
    end_date = datetime.datetime(2023, 11, 17)
    current_date = start_date
    count = 0
    maximum = 75966
    while current_date <= end_date:
        for playlist in playlists:
            for min_rank, max_rank in rank_ranges:
                list_res_json = client.list_replays(count=50,
                                min_rank=min_rank, max_rank=max_rank,
                                playlists=[playlist], replay_date_before=current_date.isoformat() + 'Z').json()
                replay_ids = replays_list_cleaner(list_res_json["list"])


                                # Pick 2 random replays from the list
                random_replays = random.sample(replay_ids, 2) if len(replay_ids) >= 2 else replay_ids
                if random_replays:
                    done, pending = await fetch_many(executer, client, random_replays)
                    dump_replays([task.result() for task in done], db, cursor)
                else:
                    print(current_date)
                print(f"Completed: {round((count/maximum)*100, 2)}%")
                
        current_date += datetime.timedelta(days=1)
