import pandas as pd

df = pd.read_csv("nyccleaned.csv")

df = df[(df["PickupBorough"] != "Unknown")]
df = df[(df["PickupBorough"] != "EWR")]
df = df[(df["payment_type"] != 3)]
df = df[(df["payment_type"] != 4)]
df = df[(df["payment_type"] != 5)]
df = df[(df["payment_type"] != 6)]


Manhattan = df[(df["PickupBorough"] == "Manhattan") & (df["DropoffBorough"] == "Manhattan")]
Bronx=df[(df["PickupBorough"]=="Bronx")&(df["DropoffBorough"]=="Bronx")]
Queens=df[(df["PickupBorough"]=="Queens")&(df["DropoffBorough"]=="Queens")]
Brooklyn=df[(df["PickupBorough"]=="Brooklyn")&(df["DropoffBorough"]=="Brooklyn")]
Staten_Island=df[(df["PickupBorough"]=="Staten Island")&(df["DropoffBorough"]=="Staten Island")]







# Mahahhtan Data
Mcash = Manhattan[(Manhattan["payment_type"] == 2)]

MHT = len(Mcash) / len(Manhattan)
print("The changce of cash payment in Manhattan " + str(MHT))
# count cash payment for Manhattan
CS = Mcash.groupby(["payment_type", "PickupZone"])["trip_distance"].count()
# count total payment for Manhattan
tt = Manhattan.groupby(["PickupZone"])["trip_distance"].count()
# % of payment use by cash
pct = CS / tt
top = pct.sort_values(ascending=False)
print("Manhattan:")
print(top)
# same for bronx
Bxcash = Bronx[(Bronx["payment_type"] == 2)]
BRX = len(Bxcash) / len(Bronx)
print("The changce of cash payment in Bronx " + str(BRX))

BCS = Bxcash.groupby(["payment_type", "PickupZone"])["trip_distance"].count()
btt = Bronx.groupby(["PickupZone"])["trip_distance"].count()
bxpct = BCS / btt
BXtop = bxpct.sort_values(ascending=False)
print("Bronx:")
print(BXtop)
# same for queens
Qcash = Queens[(Queens["payment_type"] == 2)]
QNS = len(Qcash) / len(Queens)
print("The changce of cash payment in Queens " + str(QNS))
QCS = Qcash.groupby(["payment_type", "PickupZone"])["trip_distance"].count()
qtt = Queens.groupby(["PickupZone"])["trip_distance"].count()
qpct = QCS / qtt
Qtop = qpct.sort_values(ascending=False)
print("Queens:")
print(Qtop)
#bk data
Bkcash = Brooklyn[(Brooklyn["payment_type"] == 2)]
BK  = len(Bkcash) / len(Brooklyn)
print("The changce of cash payment in Brooklyn " + str(BK))
BKCS = Bkcash.groupby(["payment_type", "PickupZone"])["trip_distance"].count()
bktt = Brooklyn.groupby(["PickupZone"])["trip_distance"].count()
bkpct = BKCS / bktt
BKtop = bkpct.sort_values(ascending=False)
print("Brooklyn:")
print(BKtop)

Scash = Staten_Island[(Staten_Island["payment_type"] == 2)]
SI = len(Scash) / len(Staten_Island)

print("The changce of cash payment in Staten_Island " + str(SI))
SCS = Scash.groupby(["payment_type", "PickupZone"])["trip_distance"].count()
stt = Staten_Island.groupby(["PickupZone"])["trip_distance"].count()
spct = SCS / stt
Stop = spct.sort_values(ascending=False)
print("Staten_Island")
print(Stop)

