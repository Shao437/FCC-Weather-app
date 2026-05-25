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

    can_travel = 'You can reach your destination'
    cannot_travel = 'You cannot reach your destination'


    if distance_miles <= 0:
        return cannot_travel
        

    elif distance_miles <= 1 and not is_raining:
        return can_travel


    elif distance_miles > 1 and distance_miles <= 6 and has_bike and not is_raining:
        return can_travel


    elif distance_miles > 6 and (has_car or has_ride_share_app):
        return can_travel
    return cannot_travel

print(can_reach_destination(distance_miles, is_raining, has_bike, has_car, has_ride_share_app))