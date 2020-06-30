ax=1
ay=1
az=1
bx=2
by=1
bz=1
cx=ay*bz-az*by
cy=az*bx-ax*bz
cz=ax*by-ay*bx
print("cx =",cx)
print("cy =",cy)
print("cz =",cz) 
print("内積",cx*ax+cy*ay+cz*az) 
