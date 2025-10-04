# data_prep/scoring.py
import pandas as pd

def calculate_player_scores(df):
    roles_weights = {
        "STR": {
          "Acc": 0, "Pac": 0, "Agi": 100, "Ant": 100, "Cmp": 100, "Dec": 0, "Det": 100,
          "Dri": 0, "Fin": 100, "Fir": 100, "OtB": 100, "Tec": 0, "Pas": 0, "Str": 0,
          "Agg": 0, "Sta": 0, "Wor": 0, "Vis": 0, "Tck": 0, "Mar": 0,
          "Bal": 0, "Bra": 0, "Cor": 0, "Cro": 0, "Cmd": 0, "Cnt": 0,
          "Fla": 0, "Fre": 0, "Hea": 50, "Jum": 0,
          "Ldr": 0, "Lon": 0, "L Th": 0, "Nat": 0, "Pen": 0, "Pos": 0,
          "Tea": 0, "Aer": 0
        }
        ,

        "W": {
          "Acc": 0, "Pac": 0, "Agi": 100, "Ant": 0, "Cmp": 0, "Dec": 0, "Det": 0,
          "Dri": 100, "Fin": 0, "Fir": 0, "OtB": 0, "Tec": 100, "Pas": 0, "Str": 0,
          "Agg": 0, "Sta": 0, "Wor": 0, "Vis": 0, "Tck": 0, "Mar": 0,
          "Bal": 100, "Bra": 0, "Cor": 0, "Cro": 0, "Cmd": 0, "Cnt": 0,
          "Fla": 100, "Fre": 0, "Hea": 0, "Jum": 0,
          "Ldr": 0, "Lon": 0, "L Th": 0, "Nat": 0, "Pen": 0, "Pos": 0,
          "Tea": 0, "Aer": 0
        }
        ,

        "CM": {
          "Acc": 0, "Pac": 0, "Agi": 0, "Ant": 0, "Cmp": 0, "Dec": 100, "Det": 0,
          "Dri": 0, "Fin": 0, "Fir": 0, "OtB": 0, "Tec": 0, "Pas": 100, "Str": 0,
          "Agg": 0, "Sta": 100, "Wor": 100, "Vis": 0, "Tck": 0, "Mar": 0,
          "Bal": 0, "Bra": 0, "Cor": 0, "Cro": 0, "Cmd": 0, "Cnt": 0,
          "Fla": 0, "Fre": 0, "Hea": 0, "Jum": 0,
          "Ldr": 0, "Lon": 0, "L Th": 0, "Nat": 0, "Pen": 0, "Pos": 0,
          "Tea": 0, "Aer": 0
        }

          #- Gets Forward Whenever Possible
          #- Tries Killer Balls Often
          #- Plays One-Twos
          #- Likes To Switch Ball To Wide Areas
          #- Arrives in Opponent's Box Late

        ,

        "DM": {
          "Acc": 0, "Pac": 0, "Agi": 0, "Ant": 0, "Cmp": 100, "Dec": 0, "Det": 0,
          "Dri": 0, "Fin": 0, "Fir": 100, "OtB": 0, "Tec": 0, "Pas": 100, "Str": 0,
          "Agg": 0, "Sta": 0, "Wor": 0, "Vis": 0, "Tck": 100, "Mar": 0,
          "Bal": 0, "Bra": 0, "Cor": 0, "Cro": 0, "Cmd": 0, "Cnt": 0,
          "Fla": 0, "Fre": 0, "Hea": 0, "Jum": 0,
          "Ldr": 0, "Lon": 0, "L Th": 0, "Nat": 0, "Pen": 0, "Pos": 100,
          "Tea": 100, "Aer": 0
        }
        ,

        "CD": {
          "Acc": 0, "Pac": 0, "Agi": 0, "Ant": 0, "Cmp": 100, "Dec": 0, "Det": 0,
          "Dri": 0, "Fin": 0, "Fir": 0, "OtB": 0, "Tec": 0, "Pas": 0, "Str": 100,
          "Agg": 0, "Sta": 0, "Wor": 0, "Vis": 0, "Tck": 100, "Mar": 0,
          "Bal": 0, "Bra": 0, "Cor": 0, "Cro": 0, "Cmd": 0, "Cnt": 100,
          "Fla": 0, "Fre": 0, "Hea": 0, "Jum": 100,
          "Ldr": 0, "Lon": 0, "L Th": 0, "Nat": 0, "Pen": 0, "Pos": 0,
          "Tea": 0, "Aer": 0
        }
        ,

        "FB": {
          "Acc": 0, "Pac": 0, "Agi": 0, "Ant": 0, "Cmp": 0, "Dec": 0, "Det": 0,
          "Dri": 0, "Fin": 0, "Fir": 0, "OtB": 0, "Tec": 0, "Pas": 0, "Str": 0,
          "Agg": 0, "Sta": 100, "Wor": 100, "Vis": 0, "Tck": 0, "Mar": 0,
          "Bal": 0, "Bra": 0, "Cor": 0, "Cro": 100, "Cmd": 0, "Cnt": 0,
          "Fla": 0, "Fre": 0, "Hea": 0, "Jum": 0,
          "Ldr": 0, "Lon": 0, "L Th": 0, "Nat": 0, "Pen": 0, "Pos": 100,
          "Tea": 0, "Aer": 0
        }
        #Attack - Technique
        #Defend - Marking
        #Support - Determination
        ,

        "GK": {
          "Acc": 0, "Pac": 0, "Agi": 100, "Ant": 0, "Cmp": 0, "Dec": 100, "Det": 0,
          "Dri": 0, "Fin": 0, "Fir": 0, "OtB": 0, "Tec": 0, "Pas": 0, "Str": 0,
          "Agg": 0, "Sta": 0, "Wor": 0, "Vis": 0, "Tck": 0, "Mar": 0,
          "Bal": 0, "Bra": 0, "Com": 0, "Cor": 0, "Cro": 0, "Cmd": 0, "Cnt": 0,
          "Ecc": 0, "Fla": 0, "Fre": 0, "Han": 0, "Hea": 0, "Jum": 100,
          "Kic": 0, "Ldr": 0, "Lon": 0, "L Th": 0, "Nat": 0, "Pen": 0, "Pos": 100,
          "Pun": 0, "Ref": 100, "1v1": 100, "TRO": 0, "Thr": 0, "Tea": 0, "Aer": 100
      }
    }

    for role, weights in roles_weights.items():
        total_w = sum(weights.values())
        def comp(row):
            t = 0
            for attr, w in weights.items():
                v = row.get(attr, 0)
                t += (0 if pd.isna(v) else v) * w
            return round(((t/total_w)*20)-121, 1) if total_w else None
        df[role] = df.apply(comp, axis=1)

    return df
