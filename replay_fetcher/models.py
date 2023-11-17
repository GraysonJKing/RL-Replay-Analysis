class CoreStats:
    def __init__(self, stats: dict) -> None:
        # Core Stats
        self.shots = stats.get("shots", None)
        self.shots_against = stats.get("shots_against", None)
        self.goals = stats.get("goals", None)
        self.goals_against = stats.get("goals_against", None)
        self.saves = stats.get("saves", None)
        self.assists = stats.get("assists", None)
        self.score = stats.get("score", None)
        self.mvp = stats.get("mvp", False)
        self.shooting_percentage = stats.get("shooting_percentage", None)

class BoostStats:
    def __init__(self, stats: dict) -> None:
        # Boost Stats
        self.bpm = stats.get("bpm", None)
        self.bcpm = stats.get("bcpm", None)
        self.avg_amount = stats.get("avg_amount", None)
        self.amount_collected = stats.get("amount_collected", None)
        self.amount_stolen = stats.get("amount_stolen", None)
        self.amount_collected_big = stats.get("amount_collected_big", None)
        self.amount_stolen_big = stats.get("amount_stolen_big", None)
        self.amount_collected_small = stats.get("amount_collected_small", None)
        self.amount_stolen_small = stats.get("amount_stolen_small", None)
        self.count_collected_big = stats.get("count_collected_big", None)
        self.count_stolen_big = stats.get("count_stolen_big", None)
        self.count_collected_small = stats.get("count_collected_small", None)
        self.count_stolen_small = stats.get("count_stolen_small", None)
        self.amount_overfill = stats.get("amount_overfill", None)
        self.amount_overfill_stolen = stats.get("amount_overfill_stolen", None)
        self.amount_used_while_supersonic = stats.get("amount_used_while_supersonic", None)
        self.time_zero_boost = stats.get("time_zero_boost", None)
        self.percent_zero_boost = stats.get("percent_zero_boost", None)
        self.time_full_boost = stats.get("time_full_boost", None)
        self.percent_full_boost = stats.get("percent_full_boost", None)
        self.time_boost_0_25 = stats.get("time_boost_0_25", None)
        self.time_boost_25_50 = stats.get("time_boost_25_50", None)
        self.time_boost_50_75 = stats.get("time_boost_50_75", None)
        self.time_boost_75_100 = stats.get("time_boost_75_100", None)
        self.percent_boost_0_25 = stats.get("percent_boost_0_25", None)
        self.percent_boost_25_50 = stats.get("percent_boost_25_50", None)
        self.percent_boost_50_75 = stats.get("percent_boost_50_75", None)
        self.percent_boost_75_100 = stats.get("percent_boost_75_100", None)

class MovementStats:
    def __init__(self, stats: dict) -> None:
        # Movement Stats
        self.avg_speed = stats.get("avg_speed", None)
        self.total_distance = stats.get("total_distance", None)
        self.time_supersonic_speed = stats.get("time_supersonic_speed", None)
        self.time_boost_speed = stats.get("time_boost_speed", None)
        self.time_slow_speed = stats.get("time_slow_speed", None)
        self.time_ground = stats.get("time_ground", None)
        self.time_low_air = stats.get("time_low_air", None)
        self.time_high_air = stats.get("time_high_air", None)
        self.time_powerslide = stats.get("time_powerslide", None)
        self.count_powerslide = stats.get("count_powerslide", None)
        self.avg_powerslide_duration = stats.get("avg_powerslide_duration", None)
        self.avg_speed_percentage = stats.get("avg_speed_percentage", None)
        self.percent_slow_speed = stats.get("percent_slow_speed", None)
        self.percent_boost_speed = stats.get("percent_boost_speed", None)
        self.percent_supersonic_speed = stats.get("percent_supersonic_speed", None)
        self.percent_ground = stats.get("percent_ground", None)
        self.percent_low_air = stats.get("percent_low_air", None)
        self.percent_high_air = stats.get("percent_high_air", None)

class PositioningStats:
    def __init__(self, stats: dict) -> None:
        # Positioning Stats
        self.avg_distance_to_ball = stats.get("avg_distance_to_ball", None)
        self.avg_distance_to_ball_possession = stats.get("avg_distance_to_ball_possession", None)
        self.avg_distance_to_ball_no_possession = stats.get("avg_distance_to_ball_no_possession", None)
        self.time_defensive_third = stats.get("time_defensive_third", None)
        self.time_neutral_third = stats.get("time_neutral_third", None)
        self.time_offensive_third = stats.get("time_offensive_third", None)
        self.time_defensive_half = stats.get("time_defensive_half", None)
        self.time_offensive_half = stats.get("time_offensive_half", None)
        self.time_behind_ball = stats.get("time_behind_ball", None)
        self.time_infront_ball = stats.get("time_infront_ball", None)
        self.time_most_back = stats.get("time_most_back", None)
        self.time_most_forward = stats.get("time_most_forward", None)
        self.goals_against_while_last_defender = stats.get("goals_against_while_last_defender", None)
        self.time_closest_to_ball = stats.get("time_closest_to_ball", None)
        self.time_farthest_from_ball = stats.get("time_farthest_from_ball", None)
        self.percent_defensive_third = stats.get("percent_defensive_third", None)
        self.percent_offensive_third = stats.get("percent_offensive_third", None)
        self.percent_neutral_third = stats.get("percent_neutral_third", None)
        self.percent_defensive_half = stats.get("percent_defensive_half", None)
        self.percent_offensive_half = stats.get("percent_offensive_half", None)
        self.percent_behind_ball = stats.get("percent_behind_ball", None)
        self.percent_infront_ball = stats.get("percent_infront_ball", None)
        self.percent_most_back = stats.get("percent_most_back", None)
        self.percent_most_forward = stats.get("percent_most_forward", None)
        self.percent_closest_to_ball = stats.get("percent_closest_to_ball", None)
        self.percent_farthest_from_ball = stats.get("percent_farthest_from_ball", None)


class DemoStats:
    def __init__(self, stats: dict) -> None:
        self.inflicted = stats.get("inflicted", None)
        self.taken = stats.get("taken", None)

class Camera:
    def __init__(self, camera: dict) -> None:
        self.fov = camera.get("fov", None)
        self.height = camera.get("height", None)
        self.pitch = camera.get("pitch", None)
        self.distance = camera.get("distance", None)
        self.stiffness = camera.get("stiffness", None)
        self.swivel_speed = camera.get("swivel_speed", None)
        self.transition_speed = camera.get("transition_speed", None)

class Player:
    def __init__(self, player: dict, colour: str) -> None:
        self.pid = player.get("id", {}).get("id", None)
        self.platform = player.get("id", {}).get("platform", None)
        self.name = player.get("name", None).replace('"', "'").replace('\\', 'backslash')
        self.player_rank = player.get("rank", {}).get("id", None)
        self.car_id = player.get("car_id", None)
        self.car = player.get("car_name", None)
        self.core_stats = CoreStats(player.get("stats", {}).get("core", {}))
        self.boost_stats = BoostStats(player.get("stats", {}).get("boost", {}))
        self.movement_stats = MovementStats(player.get("stats", {}).get("movement", {}))
        self.positioning_stats = PositioningStats(player.get("stats", {}).get("positioning", {}))
        self.demo_stats = DemoStats(player.get("stats", {}).get("demo", {}))
        self.camera = Camera(player.get("camera", {}))
        self.steering_sensitivity = player.get("steering_sensitivity", None)
        self.team_colour = colour
        self.start_time = player.get("start_time", None)
        self.end_time = player.get("end_time", None)

class Replay:
    def __init__(self, replay_data: dict) -> None:
        self.replay_id = replay_data.get("id", None)
        self.rocket_league_id = replay_data.get("rocket_league_id", None)
        self.created = replay_data.get("created", None)
        self.uploader_steam_id = replay_data.get("uploader", {}).get("steam_id", None)
        self.status = replay_data.get("status", None)
        self.match_guid = replay_data.get("match_guid", None)
        self.title = replay_data.get("title", None)
        self.map_code = replay_data.get("map_code", None) 
        self.match_type = replay_data.get("map_code", None) # Ranked
        self.team_size = replay_data.get("team_size", None)
        self.playlist_id = replay_data.get("playlist_id", None)
        self.duration = replay_data.get("duration", None)
        self.team_size = replay_data.get("team_size", None)
        self.overtime = replay_data.get("overtime", None) # Bool
        self.overtime_seconds = replay_data.get("overtime_seconds", None)
        self.season = replay_data.get("season", None)     
        self.season_type = replay_data.get("season_type", None)   
        self.date = replay_data.get("season", None)     
        self.date_has_timezone = replay_data.get("date_has_timezone", None)
        self.visibility = replay_data.get("visibility", None)
        self.min_rank_id = replay_data.get("min_rank", {}).get('id', None)
        self.max_rank_id = replay_data.get("max_rank", {}).get('id', None)
        self.map_name = replay_data.get("map_name", None)

        # Players
        self.players_blue = [Player(p, 'blue') for p in replay_data.get("blue", {}).get("players", [])]
        self.players_orange = [Player(p, 'orange') for p in replay_data.get("orange", {}).get("players", [])]

