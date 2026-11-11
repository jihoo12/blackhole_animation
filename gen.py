import random, math
random.seed(7)
W,H=1600,900; CX,CY=800,450
o=[]
a=o.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">')
a('<title>Event Horizon</title>')
a('''<defs>
<radialGradient id="bg" cx="50%" cy="50%" r="75%">
 <stop offset="0" stop-color="#1a0f2e"/><stop offset=".45" stop-color="#0a0818"/><stop offset="1" stop-color="#020206"/>
</radialGradient>
<filter id="neb" x="0" y="0" width="100%" height="100%">
 <feTurbulence type="fractalNoise" baseFrequency=".0035 .006" numOctaves="5" seed="11"/>
 <feColorMatrix values="0 0 0 0 .35  0 0 0 0 .18  0 0 0 0 .75  1.6 0 0 0 -.55"/>
 <feGaussianBlur stdDeviation="6"/>
</filter>
<filter id="neb2" x="0" y="0" width="100%" height="100%">
 <feTurbulence type="fractalNoise" baseFrequency=".005 .003" numOctaves="4" seed="42"/>
 <feColorMatrix values="0 0 0 0 .05  0 0 0 0 .55  0 0 0 0 .65  0 1.5 0 0 -.6"/>
 <feGaussianBlur stdDeviation="10"/>
</filter>
<radialGradient id="nebMaskG" cx="50%" cy="50%" r="60%">
 <stop offset="0" stop-color="#000"/><stop offset=".35" stop-color="#555"/><stop offset="1" stop-color="#fff"/>
</radialGradient>
<mask id="nebMask"><rect width="1600" height="900" fill="url(#nebMaskG)"/></mask>
<filter id="b4" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="4"/></filter>
<filter id="b14" x="-50%" y="-100%" width="200%" height="300%"><feGaussianBlur stdDeviation="14"/></filter>
<filter id="b40" x="-50%" y="-200%" width="200%" height="500%"><feGaussianBlur stdDeviation="40"/></filter>
<filter id="starGlow" x="-300%" y="-300%" width="700%" height="700%"><feGaussianBlur stdDeviation="1.6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<clipPath id="back"><rect x="0" y="-200" width="1600" height="650"/></clipPath>
<clipPath id="front"><rect x="0" y="450" width="1600" height="650"/></clipPath>
<linearGradient id="dopG" x1="0" x2="1" y1="0" y2="0">
 <stop offset="0" stop-color="#fff"/><stop offset=".5" stop-color="#ccc"/><stop offset="1" stop-color="#5a5a5a"/>
</linearGradient>
<mask id="dop" maskUnits="userSpaceOnUse" x="0" y="-200" width="1600" height="1300"><rect x="0" y="-200" width="1600" height="1300" fill="url(#dopG)"/></mask>
<linearGradient id="haloG" x1="0" x2="0" y1="0" y2="1">
 <stop offset="0" stop-color="#fff"/><stop offset=".55" stop-color="#999"/><stop offset="1" stop-color="#555"/>
</linearGradient>
<mask id="haloM" maskUnits="userSpaceOnUse" x="500" y="150" width="600" height="600"><rect x="500" y="150" width="600" height="600" fill="url(#haloG)"/></mask>
<radialGradient id="glowG"><stop offset="0" stop-color="#ffb060" stop-opacity=".55"/><stop offset=".5" stop-color="#ff5a1a" stop-opacity=".18"/><stop offset="1" stop-color="#ff3a00" stop-opacity="0"/></radialGradient>
<linearGradient id="trail" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#fff"/></linearGradient>
<radialGradient id="planetG" cx="30%" cy="30%" r="80%"><stop offset="0" stop-color="#7fd4e8"/><stop offset=".45" stop-color="#2a5f8f"/><stop offset="1" stop-color="#050a18"/></radialGradient>
<linearGradient id="sfG" gradientUnits="userSpaceOnUse" x1="0" x2="0" y1="452" y2="492"><stop offset="0" stop-color="#000"/><stop offset="1" stop-color="#fff"/></linearGradient>
<mask id="softFront" maskUnits="userSpaceOnUse" x="-200" y="-200" width="2000" height="1300"><rect x="-200" y="-200" width="2000" height="1300" fill="url(#sfG)"/></mask>
</defs>''')
a('<rect width="1600" height="900" fill="url(#bg)"/>')
a('<g mask="url(#nebMask)"><rect width="1600" height="900" filter="url(#neb)" opacity=".8"/><rect width="1600" height="900" filter="url(#neb2)" opacity=".55"/></g>')
# stars
a('<g>')
cols=['#ffffff','#ffffff','#cfe0ff','#ffe9c9','#b9c8ff']
for i in range(520):
    x=random.uniform(0,W); y=random.uniform(0,H)
    r=random.choice([.5,.6,.7,.8,1,1.1,1.4])
    op=round(random.uniform(.25,.95),2)
    c=random.choice(cols)
    if random.random()<.14:
        d=round(random.uniform(2,6),1); b=round(random.uniform(0,6),1)
        a(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r+.5:.1f}" fill="{c}" filter="url(#starGlow)"><animate attributeName="opacity" values="{op};.15;{op}" dur="{d}s" begin="-{b}s" repeatCount="indefinite"/></circle>')
    else:
        a(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{c}" opacity="{op}"/>')
a('</g>')
# a few cross-flare stars
for (x,y,s) in [(210,150,1),(1390,220,1.3),(1180,760,.9),(330,720,1.1)]:
    a(f'<g transform="translate({x},{y}) scale({s})" fill="#fff"><path d="M0-16 L1.6-1.6 L16 0 L1.6 1.6 L0 16 L-1.6 1.6 L-16 0 L-1.6-1.6Z" opacity=".9"><animateTransform attributeName="transform" type="scale" values="1;.55;1" dur="{3+s*2:.1f}s" repeatCount="indefinite"/></path><circle r="5" filter="url(#b4)"/></g>')
# shooting star
a('<g opacity="0"><rect x="-160" y="-1" width="160" height="2" rx="1" fill="url(#trail)"/><circle r="2.2" fill="#fff"/>'
  '<animateMotion path="M150,60 L620,300" dur="9s" keyTimes="0;.12;1" keyPoints="0;1;1" calcMode="linear" rotate="auto" repeatCount="indefinite"/>'
  '<animate attributeName="opacity" values="0;1;0;0" keyTimes="0;.06;.12;1" dur="9s" repeatCount="indefinite"/></g>')

def ramp(t):
    stops=[(0,(255,250,235)),(.18,(255,214,140)),(.45,(255,140,50)),(.75,(215,70,20)),(1,(110,25,30))]
    for (t0,c0),(t1,c1) in zip(stops,stops[1:]):
        if t<=t1:
            k=(t-t0)/(t1-t0); return '#%02x%02x%02x'%tuple(int(c0[i]+(c1[i]-c0[i])*k) for i in range(3))
    return '#6e191e'
def dashes():
    parts=[];tot=0
    while tot<1000:
        d=random.uniform(15,140); g=random.uniform(4,60)
        parts+= [d,g]; tot+=d+g
    k=1000/tot
    return ' '.join(f'{p*k:.1f}' for p in parts)
# disk rings
N=64; rin,rout=150,560; ratio=.17
rings=[]
for i in range(N):
    t=i/(N-1); rx=rin+(rout-rin)*t**1.15
    ry=rx*ratio
    sw=random.uniform(1.2,4.2)*(1.3-t*.5)
    op=(1-t)**.8*.85+.08
    dur=6+ (rx/rin)**1.5*5
    rings.append(f'<ellipse cx="{CX}" cy="{CY}" rx="{rx:.1f}" ry="{ry:.1f}" pathLength="1000" stroke="{ramp(t)}" stroke-width="{sw:.1f}" stroke-opacity="{op:.2f}" stroke-dasharray="{dashes()}" stroke-linecap="round"><animate attributeName="stroke-dashoffset" from="0" to="1000" dur="{dur:.1f}s" repeatCount="indefinite"/></ellipse>')
disk='<g fill="none" mask="url(#dop)">'+''.join(rings)+'</g>'
glow=(f'<ellipse cx="{CX}" cy="{CY}" rx="380" ry="65" fill="none" stroke="#ff5a1a" stroke-width="150" stroke-opacity=".16" filter="url(#b40)"/>'
      f'<ellipse cx="{CX-30}" cy="{CY}" rx="270" ry="46" fill="none" stroke="#ff9a3c" stroke-width="50" stroke-opacity=".5" filter="url(#b14)"/>'
      f'<ellipse cx="{CX-20}" cy="{CY}" rx="185" ry="31" fill="none" stroke="#ffe2b0" stroke-width="22" stroke-opacity=".7" filter="url(#b14)"/>')
a('<g transform="rotate(-9 800 450)">')
a(f'<circle cx="{CX}" cy="{CY}" r="420" fill="url(#glowG)" opacity=".5"/>')
a(f'{glow}<g clip-path="url(#back)">{disk}</g>')
# lensed halo
a(f'<ellipse cx="{CX}" cy="{CY-8}" rx="150" ry="146" fill="none" stroke="#ff8a30" stroke-width="46" opacity=".5" filter="url(#b14)" mask="url(#haloM)"/>')
a('<g fill="none" mask="url(#haloM)">')
M=22
for i in range(M):
    t=i/(M-1); r=120+62*t
    a(f'<ellipse cx="{CX}" cy="{CY-r*.07:.1f}" rx="{r:.1f}" ry="{r*.96:.1f}" pathLength="1000" stroke="{ramp(t*.8)}" stroke-width="{random.uniform(1.5,3.6):.1f}" stroke-opacity="{.95-t*.6:.2f}" stroke-dasharray="{dashes()}" stroke-linecap="round"><animate attributeName="stroke-dashoffset" from="0" to="1000" dur="{10+t*14:.1f}s" repeatCount="indefinite"/></ellipse>')
a('</g>')
# hole
a(f'<circle cx="{CX}" cy="{CY}" r="116" fill="#000"/>')
a(f'<circle cx="{CX}" cy="{CY}" r="117" fill="none" stroke="#ffd9a0" stroke-width="5" opacity=".8" filter="url(#b4)"/>')
a(f'<circle cx="{CX}" cy="{CY}" r="116.5" fill="none" stroke="#fff8ea" stroke-width="1.6"><animate attributeName="stroke-opacity" values="1;.7;1" dur="4s" repeatCount="indefinite"/></circle>')
a(f'<g mask="url(#softFront)">{glow}</g><g clip-path="url(#front)">{disk}</g>')
a('</g>')
# foreground planet
a('<g transform="translate(1330,700)"><circle r="46" fill="#3aa0c8" opacity=".25" filter="url(#b14)"/><ellipse rx="70" ry="13" fill="none" stroke="#9fd8e8" stroke-width="3" stroke-opacity=".35" transform="rotate(-18)"/><circle r="38" fill="url(#planetG)"/>'
  '<ellipse rx="70" ry="13" pathLength="100" fill="none" stroke="#9fd8e8" stroke-width="3" stroke-opacity=".6" transform="rotate(-18)" stroke-dasharray="50 50"/>'
  '<animateTransform attributeName="transform" type="translate" values="1330,700;1330,690;1330,700" dur="12s" repeatCount="indefinite"/></g>')
# vignette
a('<radialGradient id="vig" cx="50%" cy="50%" r="72%"><stop offset=".6" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".75"/></radialGradient><rect width="1600" height="900" fill="url(#vig)"/>')
a('</svg>')
open('/home/user/svgs/event-horizon.svg','w').write('\n'.join(o))
