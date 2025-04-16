% --- Facts ---
spot(sfpl_main, 'SF Public Library (Main Branch)').
spot(philz_van_ness, 'Philz Coffee (Van Ness)').
spot(capital_one_cafe, 'Capital One Cafe (Market St)').
spot(pixelcat_coffee, 'Pixelcat Coffee (Chinatown)').

cost(sfpl_main, free).
cost(philz_van_ness, purchase_required).
cost(capital_one_cafe, free).
cost(pixelcat_coffee, purchase_required).

food(sfpl_main, no).
food(philz_van_ness, yes).
food(capital_one_cafe, yes).
food(pixelcat_coffee, yes).

seating(sfpl_main, indoor).
seating(philz_van_ness, indoor).
seating(capital_one_cafe, indoor).
seating(pixelcat_coffee, indoor).

late(sfpl_main, yes).
late(philz_van_ness, no).
late(capital_one_cafe, no).
late(pixelcat_coffee, no).

wifi(sfpl_main, yes).
wifi(philz_van_ness, yes).
wifi(capital_one_cafe, yes).
wifi(pixelcat_coffee, yes).

noise(sfpl_main, quiet).
noise(philz_van_ness, lively).
noise(capital_one_cafe, lively).
noise(pixelcat_coffee, lively).

outlets(sfpl_main, yes).
outlets(philz_van_ness, yes).
outlets(capital_one_cafe, yes).
outlets(pixelcat_coffee, yes).

% --- Basic Recommendation Rule ---
% This rule requires facts like answered(cost, free) to be asserted dynamically.
recommend(SpotID, Name) :-
    spot(SpotID, Name),
    answered(cost, ReqCost), cost(SpotID, ReqCost),
    answered(noise, ReqNoise), noise(SpotID, ReqNoise),
    answered(food, ReqFood), food(SpotID, ReqFood),
    answered(late, ReqLate), late(SpotID, ReqLate),
    answered(wifi, ReqWifi), wifi(SpotID, ReqWifi),
    answered(outlets, ReqOutlets), outlets(SpotID, ReqOutlets).
