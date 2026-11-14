import json as j,os,urllib.request as u
def P(p,b):return j.load(u.urlopen(os.getenv('MAKEFUN_ENV_URL')+p,j.dumps(b).encode()))
V=[0,100,320,330,500,900,0]
T=[[ord(c)-80 for c in s]for s in('PPPPUZZ<UKFPPPPdUUZiZZdn~~~~PPPP','!,(2(<PU2UZ_2P_d2U_d2PZ_(<PP!,(2','<FFFFUPPFZZZFPZZFUUZFPUZFPPP<FFF','PPPUKPPPKPPPKPPPKPPPKPPPUZZZPPPP','<FFKFPUPFUUUPPUUKPUUFPUUFPPP<FFK','dnZPddPPF<<<22(2((!2((!2((!2((!2')]
N8=[-21,-19,-12,-8,8,12,19,21];R4=[-10,-1,1,10];B4=[-11,-9,9,11];K8=R4+B4
RM={21:2,28:1,91:8,98:4,25:3,95:12}
B=[9]*120;SD=1;C=0;EP=-1;SC=0;KS=[0,0];ST=[]
X=Exception
NB=20000;N=0
KL=[[0,0]for _ in[0]*64]
def W(p,s):a=abs(p);r=s//10-2;f=s%10-1;return(V[a]+T[a-1][(r,7-r)[p<0]*4+min(f,7-f)])*(1,-1)[p<0]
def AT(s,by):
 t=s-10*by
 if by in(B[t-1],B[t+1]):return 1
 for o in N8:
  if B[s+o]==2*by:return 1
 for o in K8:
  t=s+o
  if B[t]==6*by:return 1
  while B[t]==0:t+=o
  if B[t]*by in(5,4-(abs(o)in(9,11))):return 1
 return 0
def G(cap):
 M=[];A=M.append;Z=lambda:[A((s,t,q))for q in(5,4,3,2)]
 for s in range(21,99):
  p=B[s]
  if not 0<p*SD<7:continue
  a=abs(p)
  if a==1:
   d=10*SD;t=s+d
   if B[t]==0:
    if t>90 or t<29:Z()
    elif cap==0:A((s,t,0));s//10==3+5*(SD<0)and B[s+2*d]==0 and A((s,s+2*d,0))
   for t in(s+d-1,s+d+1):
    v=B[t]
    if-6<v*SD<0:
     if t>90 or t<29:Z()
     else:A((s,t,0))
    elif t==EP:A((s,t,0))
  elif a==2 or a==6:
   for o in(N8 if a==2 else K8):
    t=s+o;v=B[t]
    if v==cap==0 or-6<v*SD<0:A((s,t,0))
   if a==6 and cap==0 and s-25==70*(SD<0)and not AT(s,-SD):
    for d2 in(1,-1):
     k2=(1+(d2<0))*(1+3*(SD<0))
     if C&k2 and B[s+d2]==B[s+2*d2]==0 and(d2>0 or B[s-3]==0)and AT(s+d2,-SD)==AT(s+2*d2,-SD)==0:A((s,s+2*d2,0))
  else:
   for o in(R4 if a==4 else B4 if a==3 else K8):
    t=s+o
    while B[t]==0:cap==0 and A((s,t,0));t+=o
    if-6<B[t]*SD<0:A((s,t,0))
 return M
def MK(m):
 global C,EP,SC,SD
 f,t,q=m;p=B[f];d=-W(p,f);x=0;xs=-1
 if abs(p)==1 and t==EP:xs=t-10*SD;x=B[xs];d-=W(x,xs);B[xs]=0
 elif B[t]:x=B[t];xs=t;d-=W(x,t)
 B[f]=0;B[t]=SD*q if q else p;d+=W(B[t],t)
 if abs(p)==6:
  KS[SD>0]=t
  if abs(t-f)==2:
   rf=f+3-7*(t<f);rt=f+1-2*(t<f);r=B[rf];d-=W(r,rf);B[rt]=r;B[rf]=0;d+=W(r,rt)
 ST.append((x,xs,C,EP,SC));C&=~RM.get(f,0)&~RM.get(t,0);EP=f+10*SD if abs(p)==1 and abs(t-f)==20 else-1;SC+=d;SD=-SD
def UM(m):
 global C,EP,SC,SD
 SD=-SD;f,t,q=m;x,xs,C,EP,SC=ST.pop();p=SD if q else B[t]
 if abs(p)==6:
  KS[SD>0]=f
  if abs(t-f)==2:
   rf=f+3-7*(t<f);rt=f+1-2*(t<f);B[rf]=B[rt];B[rt]=0
 B[f]=p;B[t]=0
 if xs>=0:B[xs]=x
def MV(m):f,t,q=m;return V[abs(B[f])]-V[abs(B[t])]*16-900*q
def S(d,a,b,pl):
 global N;N+=1
 if N>NB:raise X
 if d<-5:return SC*SD
 chk=AT(KS[SD>0],-SD)
 if d<=0:
  if chk==0:
   st=SC*SD
   if st>=b:return b
   a=max(a,st)
  M=G(1-chk);M.sort(key=MV)
 else:M=G(0);M.sort(key=lambda m:MV(m)-9000*(m in KL[pl]))
 lg=0
 for m in M:
  MK(m)
  if AT(KS[SD<0],SD):UM(m);continue
  lg+=1;v=-S(d-1,-b,-a,pl+1);UM(m)
  if v>a:a=v
  if a>=b:KL[pl]=[m,KL[pl][0]];break
 if lg==0:return-9**5+pl if chk else(0 if d>0 else a)
 return a
def U2(x):return(ord(x[0])+10*int(x[1])-86,ord(x[2])+10*int(x[3])-86,'nbrq'.index(x[4])+2 if x[4:]else 0)
def F(fen):
 global B,SD,C,EP,SC,KS,ST
 B=[9]*120;w=fen.split();s=91;SC=0
 for ch in w[0]:
  if ch=='/':s-=18
  elif ch<'A':n=int(ch);B[s:s+n]=[0]*n;s+=n
  else:
   p=(1,-1)[ch>'Z']*('PNBRQK'.index(ch.upper())+1);B[s]=p;SC+=W(p,s)
   if abs(p)==6:KS[p>0]=s
   s+=1
 SD=(1,-1)[w[1]=='b'];C=sum(1<<'KQkq'.find(k)for k in w[2]if k!='-');EP=-1 if w[3]=='-'else ord(w[3][0])+10*int(w[3][1])-86;ST=[]
def H(fen,legal,mv):
 global N;N=0
 F(fen)
 R=[(x,U2(x))for x in legal];z=mv[-2];R=[r for r in R if r[0]!=z[2:4]+z[:2]]or R;R.sort(key=lambda r:MV(r[1]));best=R[0][0]
 for d in range(1,11):
  try:
   a=-9**6;cb=None
   for x,m in R:
    MK(m);v=-S(d-1,-9**6,-a,1);UM(m)
    if v>a:a=v;cb=x
   best=cb;R.sort(key=lambda r:r[0]!=best)
  except X:break
 return best
while 1:
 g=P('/game',{})
 if g['status']=='done':break
 while g['status']=='your_move':
  L=g['legal_moves']
  try:mv=H(g['fen'],L,g['moves'])
  except:mv=L[0]
  g=P('/move',{'game':g['game'],'move':mv})
