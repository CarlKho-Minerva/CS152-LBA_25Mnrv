% Knowledge Base for Study Spot Recommender

% Facts about study spots in the format:
% spot(ID, 'Name').
% location(ID, Distance).
% cost(ID, CostLevel).
% food(ID, FoodOption).
% seating(ID, SeatingType).
% closing_time(ID, ClosingTime).
% wifi(ID, WifiQuality).
% noise(ID, NoiseLevel).
% outlets(ID, OutletAvailability).

% Study spot IDs and names
spot(1, 'Salesforce Park').
spot(2, 'Capital One Cafe').
spot(3, 'SF Public Library').
spot(4, 'Philz Coffee').
spot(5, 'Haus Coffee').
spot(6, 'Southeast Community').
spot(7, 'Delah Coffee').
spot(8, 'Sanas Coffee').
spot(9, 'Ikea').
spot(10, 'Spro Mission').
spot(11, 'Progressive Grounds').
spot(12, 'UCSF Library').
spot(13, 'Comptons Coffee').
spot(14, 'Black Bird').
spot(15, 'Home Coffee Roast').
spot(16, 'Sight Glass').
spot(17, 'Rise and Grind').
spot(18, 'Matching Half').
spot(19, 'Ballast Coffee').

% Distances from Minerva residence
location(1, close).
location(2, close).
location(3, close).
location(4, close).
location(5, far).
location(6, far).
location(7, moderate_commute).
location(8, moderate_commute).
location(9, very_close).
location(10, far).
location(11, far).
location(12, far).
location(13, far).
location(14, far).
location(15, close).
location(16, close).
location(17, far).
location(18, far).
location(19, far).

% Cost levels
cost(1, low).
cost(2, medium).
cost(3, low).
cost(4, medium).
cost(5, medium).
cost(6, low).
cost(7, high).
cost(8, high).
cost(9, low).
cost(10, high).
cost(11, medium).
cost(12, low).
cost(13, medium).
cost(14, medium).
cost(15, medium).
cost(16, medium).
cost(17, high).
cost(18, high).
cost(19, medium).

% Food options
food(1, none).
food(2, full_menu).
food(3, snacks_only).
food(4, full_menu).
food(5, full_menu).
food(6, coffee_only).
food(7, full_menu).
food(8, full_menu).
food(9, full_menu).
food(10, full_menu).
food(11, full_menu).
food(12, coffee_only).
food(13, full_menu).
food(14, full_menu).
food(15, full_menu).
food(16, full_menu).
food(17, full_menu).
food(18, full_menu).
food(19, full_menu).

% Seating types - multiple options per spot
seating(1, outdoor_seating).
seating(2, private_study_rooms).
seating(2, shared_long_tables).
seating(3, quiet_individual).
seating(3, shared_long_tables).
seating(3, comfortable_lounge).
seating(4, comfortable_lounge).
seating(4, outdoor_seating).
seating(4, shared_long_tables).
seating(4, regular_tables).
seating(5, shared_long_tables).
seating(5, comfortable_lounge).
seating(5, outdoor_seating).
seating(5, regular_tables).
seating(6, shared_long_tables).
seating(6, outdoor_seating).
seating(7, comfortable_lounge).
seating(7, regular_tables).
seating(8, comfortable_lounge).
seating(8, regular_long_tables).
seating(8, shared_long_tables).
seating(9, shared_long_tables).
seating(9, regular_tables).
seating(10, outdoor_seating).
seating(10, regular_tables).
seating(11, shared_long_tables).
seating(11, outdoor_seating).
seating(11, comfortable_lounge).
seating(11, regular_tables).
seating(12, quiet_individual).
seating(12, shared_long_tables).
seating(12, comfortable_lounge).
seating(12, regular_tables).
seating(13, shared_long_tables).
seating(13, comfortable_lounge).
seating(13, outdoor_seating).
seating(14, comfortable_lounge).
seating(14, outdoor_seating).
seating(15, shared_long_tables).
seating(15, comfortable_lounge).
seating(16, shared_long_tables).
seating(17, shared_long_tables).
seating(18, regular_tables).
seating(18, comfortable_lounge).
seating(19, shared_long_tables).

% Closing times
closing_time(1, closes_8_10pm).
closing_time(2, closes_before_8pm).
closing_time(3, closes_8_10pm).
closing_time(4, closes_before_8pm).
closing_time(5, closes_before_5pm).
closing_time(6, closes_before_5pm).
closing_time(7, closes_before_8pm).
closing_time(8, open_until_midnight).
closing_time(9, closes_before_8pm).
closing_time(10, closes_before_5pm).
closing_time(11, closes_before_8pm).
closing_time(12, closes_before_8pm).
closing_time(13, closes_before_5pm).
closing_time(14, closes_before_8pm).
closing_time(15, closes_before_5pm).
closing_time(16, closes_before_5pm).
closing_time(17, closes_before_5pm).
closing_time(18, closes_before_5pm).
closing_time(19, closes_before_5pm).

% WiFi quality
wifi(1, poor).
wifi(2, good).
wifi(3, good).
wifi(4, good).
wifi(5, good).
wifi(6, good).
wifi(7, good).
wifi(8, good).
wifi(9, good).
wifi(10, good).
wifi(11, good).
wifi(12, good).
wifi(13, good).
wifi(14, none).
wifi(15, good).
wifi(16, none).
wifi(17, good).
wifi(18, poor).
wifi(19, good).

% Noise levels
noise(1, low).
noise(2, moderate).
noise(3, silent).
noise(4, moderate).
noise(5, low).
noise(6, moderate).
noise(7, moderate).
noise(8, high).
noise(9, moderate).
noise(10, high).
noise(11, low).
noise(12, silent).
noise(13, moderate).
noise(14, moderate).
noise(15, moderate).
noise(16, moderate).
noise(17, moderate).
noise(18, moderate).
noise(19, moderate).

% Outlet availability
outlets(1, none).
outlets(2, many).
outlets(3, every_seat).
outlets(4, few).
outlets(5, many).
outlets(6, few).
outlets(7, many).
outlets(8, many).
outlets(9, few).
outlets(10, many).
outlets(11, few).
outlets(12, few).
outlets(13, few).
outlets(14, few).
outlets(15, many).
outlets(16, few).
outlets(17, few).
outlets(18, few).
outlets(19, many).

% Helper predicate to check list membership
member(X, [X|_]).
member(X, [_|T]) :- member(X, T).

% Core recommendation rule
recommend(SpotID, Name) :-
    % Get the spot's name
    spot(SpotID, Name),
    
    % Check if all answered criteria match
    (answered(location, Loc) -> location(SpotID, Loc) ; true),
    (answered(cost, Cost) -> cost(SpotID, Cost) ; true),
    (answered(food, Food) -> food(SpotID, Food) ; true),
    (answered(seating, Seat) -> seating(SpotID, Seat) ; true),
    (answered(closing_time, Close) -> closing_time(SpotID, Close) ; true),
    (answered(wifi, Wifi) -> wifi(SpotID, Wifi) ; true),
    (answered(noise, Noise) -> noise(SpotID, Noise) ; true),
    (answered(outlets, Outlet) -> outlets(SpotID, Outlet) ; true).

% Test cases
test_case(1, "Quiet, free, near campus") :- 
    assert(answered(noise, silent)),
    assert(answered(cost, low)),
    assert(answered(location, close)).

test_case(2, "Lively cafe, outlets needed, Mission") :-
    assert(answered(noise, high)),
    assert(answered(outlets, many)),
    assert(answered(location, far)),
    assert(answered(wifi, good)).

test_case(3, "Outdoor, food available, any cost") :-
    assert(answered(seating, outdoor_seating)),
    assert(answered(food, full_menu)).

% Clear test case assertions
clear_test :-
    retractall(answered(_, _)). 