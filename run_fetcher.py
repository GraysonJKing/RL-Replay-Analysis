import datetime
from replay_fetcher import fetcher
from replay_fetcher import models
import pychasing
import asyncio
import json
import mysql.connector
from dotenv import load_dotenv
import os


# Insert data to DB
def dump_replays(replays: list[models.Replay], db, cursor) -> None:
    for replay in replays:
        try:
            insert_replay(cursor, replay)
            
            for player in replay.players_blue + replay.players_orange:
                insert_player(cursor, player, replay.replay_id)
            
            db.commit()
        except mysql.connector.Error as err:
            print(f"An error occurred: {err}")
            db.rollback()


def insert_replay(cursor, replay):
    replay_query = """
    INSERT INTO replays (replay_id, rocket_league_id, created, uploader_steam_id, status, match_guid, title, map_code, match_type, team_size, playlist_id, duration, overtime, overtime_seconds, season, season_type, date, date_has_timezone, visibility, min_rank_id, max_rank_id, map_name)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    replay_values = (
        replay.replay_id,
        replay.rocket_league_id,
        replay.created[:10],
        replay.uploader_steam_id,
        replay.status,
        replay.match_guid,
        replay.title,
        replay.map_code,
        replay.match_type,
        replay.team_size,
        replay.playlist_id,
        replay.duration,
        replay.overtime,
        replay.overtime_seconds,
        replay.season,
        replay.season_type,
        replay.date,
        replay.date_has_timezone,
        replay.visibility,
        replay.min_rank_id,
        replay.max_rank_id,
        replay.map_name
    )
    cursor.execute(replay_query, replay_values)

def insert_stats(cursor, player, replay_id):
    stats_query = """
    INSERT INTO stats (player_id, platform, replay_id, shots, shots_against, goals, goals_against, saves, assists, score, mvp, shooting_percentage, bpm, bcpm, avg_amount, amount_collected, amount_stolen, amount_collected_big, amount_stolen_big, amount_collected_small, amount_stolen_small, count_collected_big, count_stolen_big, count_collected_small, count_stolen_small, amount_overfill, amount_overfill_stolen, amount_used_while_supersonic, time_zero_boost, percent_zero_boost, time_full_boost, percent_full_boost, time_boost_0_25, time_boost_25_50, time_boost_50_75, time_boost_75_100, percent_boost_0_25, percent_boost_25_50, percent_boost_50_75, percent_boost_75_100, avg_speed, total_distance, time_supersonic_speed, time_boost_speed, time_slow_speed, time_ground, time_low_air, time_high_air, time_powerslide, count_powerslide, avg_powerslide_duration, avg_speed_percentage, percent_slow_speed, percent_boost_speed, percent_supersonic_speed, percent_ground, percent_low_air, percent_high_air, avg_distance_to_ball, avg_distance_to_ball_possession, avg_distance_to_ball_no_possession, time_defensive_third, time_neutral_third, time_offensive_third, time_defensive_half, time_offensive_half, time_behind_ball, time_infront_ball, time_most_back, time_most_forward, goals_against_while_last_defender, time_closest_to_ball, time_farthest_from_ball, percent_defensive_third, percent_offensive_third, percent_neutral_third, percent_defensive_half, percent_offensive_half, percent_behind_ball, percent_infront_ball, percent_most_back, percent_most_forward, percent_closest_to_ball, percent_farthest_from_ball, inflicted, taken) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    mvp_int = 1 if player.core_stats.mvp else 0
    stats_values = (
        player.pid,
        player.platform,
        replay_id,
        player.core_stats.shots,
        player.core_stats.shots_against,
        player.core_stats.goals,
        player.core_stats.goals_against,
        player.core_stats.saves,
        player.core_stats.assists,
        player.core_stats.score,
        mvp_int,
        player.core_stats.shooting_percentage,
        player.boost_stats.bpm,
        player.boost_stats.bcpm,
        player.boost_stats.avg_amount,
        player.boost_stats.amount_collected,
        player.boost_stats.amount_stolen,
        player.boost_stats.amount_collected_big,
        player.boost_stats.amount_stolen_big,
        player.boost_stats.amount_collected_small,
        player.boost_stats.amount_stolen_small,
        player.boost_stats.count_collected_big,
        player.boost_stats.count_stolen_big,
        player.boost_stats.count_collected_small,
        player.boost_stats.count_stolen_small,
        player.boost_stats.amount_overfill,
        player.boost_stats.amount_overfill_stolen,
        player.boost_stats.amount_used_while_supersonic,
        player.boost_stats.time_zero_boost,
        player.boost_stats.percent_zero_boost,
        player.boost_stats.time_full_boost,
        player.boost_stats.percent_full_boost,
        player.boost_stats.time_boost_0_25,
        player.boost_stats.time_boost_25_50,
        player.boost_stats.time_boost_50_75,
        player.boost_stats.time_boost_75_100,
        player.boost_stats.percent_boost_0_25,
        player.boost_stats.percent_boost_25_50,
        player.boost_stats.percent_boost_50_75,
        player.boost_stats.percent_boost_75_100,
        player.movement_stats.avg_speed,
        player.movement_stats.total_distance,
        player.movement_stats.time_supersonic_speed,
        player.movement_stats.time_boost_speed,
        player.movement_stats.time_slow_speed,
        player.movement_stats.time_ground,
        player.movement_stats.time_low_air,
        player.movement_stats.time_high_air,
        player.movement_stats.time_powerslide,
        player.movement_stats.count_powerslide,
        player.movement_stats.avg_powerslide_duration,
        player.movement_stats.avg_speed_percentage,
        player.movement_stats.percent_slow_speed,
        player.movement_stats.percent_boost_speed,
        player.movement_stats.percent_supersonic_speed,
        player.movement_stats.percent_ground,
        player.movement_stats.percent_low_air,
        player.movement_stats.percent_high_air,
        player.positioning_stats.avg_distance_to_ball,
        player.positioning_stats.avg_distance_to_ball_possession,
        player.positioning_stats.avg_distance_to_ball_no_possession,
        player.positioning_stats.time_defensive_third,
        player.positioning_stats.time_neutral_third,
        player.positioning_stats.time_offensive_third,
        player.positioning_stats.time_defensive_half,
        player.positioning_stats.time_offensive_half,
        player.positioning_stats.time_behind_ball,
        player.positioning_stats.time_infront_ball,
        player.positioning_stats.time_most_back,
        player.positioning_stats.time_most_forward,
        player.positioning_stats.goals_against_while_last_defender,
        player.positioning_stats.time_closest_to_ball,
        player.positioning_stats.time_farthest_from_ball,
        player.positioning_stats.percent_defensive_third,
        player.positioning_stats.percent_offensive_third,
        player.positioning_stats.percent_neutral_third,
        player.positioning_stats.percent_defensive_half,
        player.positioning_stats.percent_offensive_half,
        player.positioning_stats.percent_behind_ball,
        player.positioning_stats.percent_infront_ball,
        player.positioning_stats.percent_most_back,
        player.positioning_stats.percent_most_forward,
        player.positioning_stats.percent_closest_to_ball,
        player.positioning_stats.percent_farthest_from_ball,
        player.demo_stats.inflicted,
        player.demo_stats.taken
    )

    
    cursor.execute(stats_query, stats_values)

def insert_player(cursor, player, replay_id):
    player_query = """
    INSERT INTO players (player_id, platform, replay_id, name, player_rank, car_id, car_name, fov, 
                         height, pitch, distance, stiffness, swivel_speed, transition_speed, 
                         steering_sensitivity, team_colour, mvp, start_time, end_time)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    mvp_value = 1 if player.core_stats.mvp else 0

    player_values = (
        player.pid,
        player.platform,
        replay_id,
        player.name,
        player.player_rank,
        player.car_id,
        player.car,
        player.camera.fov,
        player.camera.height,
        player.camera.pitch,
        player.camera.distance,
        player.camera.stiffness,
        player.camera.swivel_speed,
        player.camera.transition_speed,
        player.steering_sensitivity,
        player.team_colour,
        mvp_value,
        player.start_time,
        player.end_time
    )
    cursor.execute(player_query, player_values)
    insert_stats(cursor, player, replay_id)

if __name__ == '__main__':
    load_dotenv()
    ballchasing_api = os.getenv("APIKEY")
    client = pychasing.Client(ballchasing_api, True,
                            pychasing.PatreonTier.champion)
    replay_batch_size = 6
    max_workers = 5
    asyncio.run(fetcher.start(dump_replays, client,
                            replay_batch_size, max_workers))

