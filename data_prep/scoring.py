# data_prep/scoring.py
import pandas as pd

def calculate_player_scores(df):
    roles_weights = {
        "STR": {
          "Acc": 80, "Pac": 80, "Agi": 100, "Ant": 50, "Cmp": 100, "Dec": 50, "Det": 50,
          "Dri": 0, "Fin": 100, "Fir": 90, "OtB": 100, "Tec": 0, "Pas": 0, "Str": 90,
          "Agg": 100, "Sta": 50, "Wor": 50, "Vis": 0, "Tck": 0, "Mar": 0,
          "Bal": 50, "Bra": 0, "Cor": 0, "Cro": 0, "Cmd": 0, "Cnt": 0,
          "Fla": 50, "Fre": 0, "Hea": 50, "Jum": 50,
          "Ldr": 70, "Lon": 0, "L Th": 0, "Nat": 0, "Pen": 0, "Pos": 0,
          "Tea": 0, "Aer": 0
        }
        ,

        "W": {
          "Acc": 100, "Pac": 90, "Agi": 100, "Ant": 50, "Cmp": 90, "Dec": 90, "Det": 30,
          "Dri": 100, "Fin": 50, "Fir": 90, "OtB": 100, "Tec": 100, "Pas": 50, "Str": 30,
          "Agg": 0, "Sta": 50, "Wor": 50, "Vis": 50, "Tck": 0, "Mar": 0,
          "Bal": 50, "Bra": 0, "Cor": 0, "Cro": 30, "Cmd": 0, "Cnt": 0,
          "Fla": 50, "Fre": 0, "Hea": 30, "Jum": 30,
          "Ldr": 0, "Lon": 0, "L Th": 0, "Nat": 0, "Pen": 0, "Pos": 0,
          "Tea": 0, "Aer": 0
        }
        ,

        "CM": {
          "Acc": 100, "Pac": 90, "Agi": 90, "Ant": 90, "Cmp": 100, "Dec": 100, "Det": 30,
          "Dri": 90, "Fin": 30, "Fir": 90, "OtB": 100, "Tec": 100, "Pas": 100, "Str": 50,
          "Agg": 50, "Sta": 100, "Wor": 100, "Vis": 100, "Tck": 60, "Mar": 30,
          "Bal": 50, "Bra": 60, "Cor": 30, "Cro": 30, "Cmd": 0, "Cnt": 90,
          "Fla": 60, "Fre": 40, "Hea": 30, "Jum": 30,
          "Ldr": 40, "Lon": 70, "L Th": 0, "Nat": 60, "Pen": 30, "Pos": 80,
          "Tea": 50, "Aer": 30
        }

        ,

        "DM": {
          "Acc": 70, "Pac": 65, "Agi": 70, "Ant": 100, "Cmp": 85, "Dec": 95, "Det": 90,
          "Dri": 30, "Fin": 5, "Fir": 75, "OtB": 40, "Tec": 70, "Pas": 85, "Str": 85,
          "Agg": 95, "Sta": 100, "Wor": 95, "Vis": 70, "Tck": 100, "Mar": 95,
          "Bal": 80, "Bra": 80, "Cor": 30, "Cro": 20, "Cmd": 0, "Cnt": 70,
          "Fla": 20, "Fre": 25, "Hea": 65, "Jum": 70,
          "Ldr": 70, "Lon": 55, "L Th": 10, "Nat": 80, "Pen": 20, "Pos": 100,
          "Tea": 95, "Aer": 60
        }
        ,

        "CD": {
          "Acc": 50, "Pac": 50, "Agi": 30, "Ant": 100, "Cmp": 90, "Dec": 90, "Det": 30,
          "Dri": 30, "Fin": 0,  "Fir": 90, "OtB": 30, "Tec": 90, "Pas": 90, "Str": 90,
          "Agg": 50, "Sta": 50, "Wor": 50, "Vis": 50, "Tck": 70, "Mar": 100,
          "Bal": 50, "Bra": 70, "Cor": 0, "Cro": 0, "Cmd": 30, "Cnt": 50,
          "Fla": 0, "Fre": 0, "Hea": 60, "Jum": 90,
          "Ldr": 50, "Lon": 30, "L Th": 0, "Nat": 50, "Pen": 0, "Pos": 100,
          "Tea": 40, "Aer": 80
        }

        ,

        "FB": {
          "Acc": 100, "Pac": 100, "Agi": 50, "Ant": 90, "Cmp": 90, "Dec": 90, "Det": 30,
          "Dri": 50, "Fin": 0,  "Fir": 90, "OtB": 100, "Tec": 90, "Pas": 90, "Str": 50,
          "Agg": 50, "Sta": 100, "Wor": 100, "Vis": 50, "Tck": 60, "Mar": 50,
          "Bal": 50, "Bra": 50, "Cor": 30, "Cro": 90, "Cmd": 0, "Cnt": 50,
          "Fla": 30, "Fre": 30, "Hea": 30, "Jum": 30,
          "Ldr": 30, "Lon": 30, "L Th": 0, "Nat": 50, "Pen": 0, "Pos": 90,
          "Tea": 60, "Aer": 30
        }

        ,

        "GK": {
          "Acc": 0, "Pac": 0, "Agi": 0, "Ant": 0, "Cmp": 0, "Dec": 100, "Det": 0,
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
