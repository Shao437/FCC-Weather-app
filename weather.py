CAN_TRAVEL = 'You can reach your destination'
CANNOT_TRAVEL = 'You cannot reach your destination'

distance_miles = 1
is_raining = False
has_bike = False
has_car = True
has_ride_share_app = True


def can_reach_destination(
        distance_miles: int, 
        is_raining: bool, 
        has_bike: bool, 
        has_car: bool, 
        has_ride_share_app: bool
        ) -> str: 
    '''
    Determine whether the user can reach their destination based on the distance, 
    weather, available transportation options and weather travel app
    '''

    if distance_miles <= 0:
        return CANNOT_TRAVEL

    elif distance_miles <= 1:
        return CAN_TRAVEL if not is_raining else CANNOT_TRAVEL

    elif distance_miles > 1:
        return CAN_TRAVEL if has_bike and not is_raining else CANNOT_TRAVEL

    elif distance_miles > 6 and has_car or has_ride_share_app:
        return CAN_TRAVEL
    
    return CANNOT_TRAVEL

print(can_reach_destination(distance_miles, is_raining, has_bike, has_car, has_ride_share_app))
