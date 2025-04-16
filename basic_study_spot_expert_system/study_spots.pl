% study_spots.pl - Minimal Prolog KB for Study Spot Recommender

% study_spot(Name, Free, Food, Seating, LateNight, Wifi, Distance, Atmosphere, Power).
study_spot(library, yes, no, quiet, no, yes, short, silent, yes).
study_spot(cafe, no, yes, casual, yes, yes, medium, lively, yes).
study_spot(student_center, yes, yes, casual, yes, yes, short, social, yes).
study_spot(park, yes, no, outdoor, no, no, long, relaxed, no).

% Askable values for each attribute:
askable(free, [yes, no]).
askable(food, [yes, no]).
askable(seating, [quiet, casual, outdoor]).
askable(latenight, [yes, no]).
askable(wifi, [yes, no]).
askable(distance, [short, medium, long]).
askable(atmosphere, [silent, lively, social, relaxed]).
askable(power, [yes, no]).
