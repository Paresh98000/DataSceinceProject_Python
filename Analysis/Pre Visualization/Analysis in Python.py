Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Users\Hp\OneDrive\MCA\Sem 4\Data Science Project\data.csv\Clubewise player.py 
Path is seted :  C:\Users\Hp\OneDrive\MCA\Sem 4\Data Science Project\data.csv\Football Data New Excel Format.xlsx
Traceback (most recent call last):
  File "C:\Users\Hp\OneDrive\MCA\Sem 4\Data Science Project\data.csv\Clubewise player.py", line 25, in <module>
    str1 = clubs[x]+","+str(counts[x])
TypeError: can only concatenate str (not "int") to str
>>> 
 RESTART: C:\Users\Hp\OneDrive\MCA\Sem 4\Data Science Project\data.csv\Clubewise player.py 
Path is seted :  C:\Users\Hp\OneDrive\MCA\Sem 4\Data Science Project\data.csv\Football Data New Excel Format.xlsx
Derry City,18
Limerick FC,19
Sligo Rovers,19
América FC (Minas Gerais),20
Atlético Mineiro,20
Atlético Paranaense,20
Bahia,20
Botafogo,20
Ceará Sporting Club,20
Chapecoense,20
Cruzeiro,20
Fluminense,20
Grêmio,20
Internacional,20
Paraná,20
Santos,20
Sport Club do Recife,20
Tromsø IL,20
Vitória,20
Dalkurd FF,21
Melbourne Victory,21
Wellington Phoenix,21
FK Haugesund,22
Shamrock Rovers,22
Östersunds FK,22
AC Ajaccio,23
Bray Wanderers,23
Brisbane Roar,23
Chicago Fire,23
Clube Sport Marítimo,23
Colorado Rapids,23
Dundalk,23
FC København,23
GFC Ajaccio,23
GIF Sundsvall,23
IFK Göteborg,23
Traceback (most recent call last):
  File "C:\Users\Hp\OneDrive\MCA\Sem 4\Data Science Project\data.csv\Clubewise player.py", line 26, in <module>
    file.write(str1)
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\encodings\cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
UnicodeEncodeError: 'charmap' codec can't encode character '\u015f' in position 7: character maps to <undefined>
>>> 
 RESTART: C:\Users\Hp\OneDrive\MCA\Sem 4\Data Science Project\data.csv\Clubewise player.py 
Path is seted :  C:\Users\Hp\OneDrive\MCA\Sem 4\Data Science Project\data.csv\Football Data New Excel Format.xlsx
Derry City,18
Limerick FC,19
Sligo Rovers,19
América FC (Minas Gerais),20
Atlético Mineiro,20
Atlético Paranaense,20
Bahia,20
Botafogo,20
Ceará Sporting Club,20
Chapecoense,20
Cruzeiro,20
Fluminense,20
Grêmio,20
Internacional,20
Paraná,20
Santos,20
Sport Club do Recife,20
Tromsø IL,20
Vitória,20
Dalkurd FF,21
Melbourne Victory,21
Wellington Phoenix,21
FK Haugesund,22
Shamrock Rovers,22
Östersunds FK,22
AC Ajaccio,23
Bray Wanderers,23
Brisbane Roar,23
Chicago Fire,23
Clube Sport Marítimo,23
Colorado Rapids,23
Dundalk,23
FC København,23
GFC Ajaccio,23
GIF Sundsvall,23
IFK Göteborg,23
Traceback (most recent call last):
  File "C:\Users\Hp\OneDrive\MCA\Sem 4\Data Science Project\data.csv\Clubewise player.py", line 26, in <module>
    file.write(str1)
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\encodings\cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
UnicodeEncodeError: 'charmap' codec can't encode character '\u015f' in position 7: character maps to <undefined>
>>> file.close()
>>> 
 RESTART: C:\Users\Hp\OneDrive\MCA\Sem 4\Data Science Project\data.csv\Clubewise player.py 
Path is seted :  C:\Users\Hp\OneDrive\MCA\Sem 4\Data Science Project\data.csv\Football Data New Excel Format.xlsx
Traceback (most recent call last):
  File "C:\Users\Hp\OneDrive\MCA\Sem 4\Data Science Project\data.csv\Clubewise player.py", line 23, in <module>
    file.write("Club,Total_Players")
TypeError: a bytes-like object is required, not 'str'
>>> 
 RESTART: C:\Users\Hp\OneDrive\MCA\Sem 4\Data Science Project\data.csv\Clubewise player.py 
Path is seted :  C:\Users\Hp\OneDrive\MCA\Sem 4\Data Science Project\data.csv\Football Data New Excel Format.xlsx
Derry City,18

Limerick FC,19

Sligo Rovers,19

América FC (Minas Gerais),20

Atlético Mineiro,20

Atlético Paranaense,20

Bahia,20

Botafogo,20

Ceará Sporting Club,20

Chapecoense,20

Cruzeiro,20

Fluminense,20

Grêmio,20

Internacional,20

Paraná,20

Santos,20

Sport Club do Recife,20

Tromsø IL,20

Vitória,20

Dalkurd FF,21

Melbourne Victory,21

Wellington Phoenix,21

FK Haugesund,22

Shamrock Rovers,22

Östersunds FK,22

AC Ajaccio,23

Bray Wanderers,23

Brisbane Roar,23

Chicago Fire,23

Clube Sport Marítimo,23

Colorado Rapids,23

Dundalk,23

FC København,23

GFC Ajaccio,23

GIF Sundsvall,23

IFK Göteborg,23

Kasimpaşa SK,23

Odds BK,23

St. Patrick's Athletic,23

AS Saint-Étienne,24

Atalanta,24

BSC Young Boys,24

Cagliari,24

Cheltenham Town,24

Crawley Town,24

Crotone,24

Fiorentina,24

Forest Green Rovers,24

IFK Norrköping,24

IK Start,24

Inter,24

Kristiansund BK,24

LASK Linz,24

La Berrichonne de Châteauroux,24

Lillestrøm SK,24

Newcastle Jets,24

Os Belenenses,24

Ranheim Fotball,24

SG Sonnenhof Großaspach,24

SV Wehen Wiesbaden,24

Sandefjord Fotball,24

Strømsgodset IF,24

VfR Aalen,24

Viktoria Plzeň,24

AC Horsens,25

Adelaide United,25

BB Erzurumspor,25

Benevento,25

Bohemian FC,25

CA Osasuna,25

CD Tondela,25

Carlisle United,25

Central Coast Mariners,25

Clermont Foot 63,25

Cork City,25

Cruz Azul,25

Djurgårdens IF,25

En Avant de Guingamp,25

Esbjerg fB,25

FC Hansa Rostock,25

FC St. Gallen,25

FSV Zwickau,25

GD Chaves,25

Grimsby Town,25

Hallescher FC,25

Hibernian,25

Hobro IK,25

Juventus,25

KRC Genk,25

Kayserispor,25

LA Galaxy,25

LOSC Lille,25

Los Angeles FC,25

Luton Town,25

Melbourne City FC,25

Moreirense FC,25

Napoli,25

Ohod Club,25

Oldham Athletic,25

Paris FC,25

Perth Glory,25

Randers FC,25

River Plate,25

Royal Antwerp FC,25

SK Sturm Graz,25

Stade Brestois 29,25

Sydney FC,25

US Cremonese,25

US Orléans Loiret Football,25

Waterford FC,25

Western Sydney Wanderers,25

Wycombe Wanderers,25

Zagłębie Sosnowiec,25

Śląsk Wrocław,25

1. FC Kaiserslautern,26

1. FC Magdeburg,26

AFC Wimbledon,26

AS Béziers,26

Akhisar Belediyespor,26

Bayer 04 Leverkusen,26

CD Feirense,26

CD Nacional,26

CF Rayo Majadahonda,26

Columbus Crew SC,26

Córdoba CF,26

Dijon FCO,26

Elche CF,26

Excelsior,26

FC Groningen,26

FC Metz,26

FC Thun,26

FC Utrecht,26

Grenoble Foot 38,26

HJK Helsinki,26

IF Brommapojkarna,26

KV Oostende,26

MSV Duisburg,26

Macclesfield Town,26

Molde FK,26

Monterrey,26

New York City FC,26

Newport County,26

Perugia,26

Peterborough United,26

Pogoń Szczecin,26

Port Vale,26

Roma,26

Rosenborg BK,26

Rotherham United,26

SC Fortuna Köln,26

SCR Altach,26

SV Zulte-Waregem,26

San Jose Earthquakes,26

Sanfrecce Hiroshima,26

Santa Clara,26

Santos Laguna,26

Sarpsborg 08 FF,26

SpVgg Unterhaching,26

Swindon Town,26

TSV Hartberg,26

Tianjin Quanjian FC,26

Torino,26

VVV-Venlo,26

VfL Bochum 1848,26

VfL Osnabrück,26

Vålerenga Fotball,26

Wisła Kraków,26

Wisła Płock,26

Wolfsberger AC,26

AIK,27

AJ Auxerre,27

Aalborg BK,27

Aarhus GF,27

Aberdeen,27

Arka Gdynia,27

Atiker Konyaspor,27

BK Häcken,27

Belgrano de Córdoba,27

Boavista FC,27

Boca Juniors,27

Brøndby IF,27

CD Everton de Viña del Mar,27

CD Huachipato,27

CD Universidad de Concepción,27

Club Atlético Banfield,27

Cracovia,27

Deportivo Alavés,27

Dundee FC,27

FC Admira Wacker Mödling,27

FC Basel 1893,27

FC Lugano,27

FC Luzern,27

FC Midtjylland,27

FC Nordsjælland,27

FC Red Bull Salzburg,27

FC Sion,27

FC Wacker Innsbruck,27

FC Würzburger Kickers,27

FC Zürich,27

FK Austria Wien,27

FK Bodø/Glimt,27

Foggia,27

Fortuna Sittard,27

Genoa,27

Grasshopper Club Zürich,27

Górnik Zabrze,27

Hammarby IF,27

Heart of Midlothian,27

IF Elfsborg,27

IK Sirius,27

Jagiellonia Białystok,27

Kaizer Chiefs,27

Kalmar FF,27

Korona Kielce,27

Lech Poznań,27

Lechia Gdańsk,27

Legia Warszawa,27

Lobos BUAP,27

Malmö FF,27

Miedź Legnica,27

Milan,27

Nagoya Grampus,27

Neuchâtel Xamax,27

New England Revolution,27

Nîmes Olympique,27

Odense Boldklub,27

PAOK,27

PEC Zwolle,27

Piast Gliwice,27

Pohang Steelers,27

Portimonense SC,27

Real Betis,27

SC Heerenveen,27

SC Preußen Münster,27

SK Brann,27

SK Rapid Wien,27

SKN St. Pölten,27

SPAL,27

SV Darmstadt 98,27

SV Mattersburg,27

Sampdoria,27

Sassuolo,27

Scunthorpe United,27

Seattle Sounders FC,27

Shandong Luneng TaiShan FC,27

Shrewsbury,27

Sivasspor,27

Spartak Moscow,27

Sporting Kansas City,27

St. Johnstone FC,27

St. Mirren,27

Stabæk Fotball,27

Stade Rennais FC,27

SønderjyskE,27

Trelleborgs FF,27

Unión La Calera,27

Urawa Red Diamonds,27

Vancouver Whitecaps FC,27

Vegalta Sendai,27

Vejle Boldklub,27

Vendsyssel FF,27

VfB Stuttgart,27

Walsall,27

Zagłębie Lubin,27

Örebro SK,27

1. FC Heidenheim 1846,28

1. FC Köln,28

1. FC Union Berlin,28

ADO Den Haag,28

AEK Athens,28

Accrington Stanley,28

Al Fateh,28

Al Fayha,28

Alianza Petrolera,28

América de Cali,28

Argentinos Juniors,28

Atlético Bucaramanga,28

Atlético Huila,28

Atlético Nacional,28

Atlético Tucumán,28

Audax Italiano,28

Barnsley,28

Beijing Renhe FC,28

Beijing Sinobo Guoan FC,28

Beşiktaş JK,28

Blackpool,28

Bologna,28

Boyacá Chicó FC,28

Bradford City,28

Bristol Rovers,28

Burton Albion,28

Bury,28

CD Antofagasta,28

CD Aves,28

CD Numancia,28

CD O'Higgins,28

CD Palestino,28

CF Reus Deportiu,28

Cambridge United,28

Celtic,28

Chamois Niortais Football Club,28

Changchun Yatai FC,28

Charlton Athletic,28

Chievo Verona,28

Chongqing Dangdai Lifan FC SWM Team,28

Club Atlético Aldosivi,28

Club Atlético Colón,28

Club Atlético Huracán,28

Club Atlético Lanús,28

Club Atlético Talleres,28

Club Atlético Tigre,28

Club Brugge KV,28

Club Deportes Temuco,28

Club Tijuana,28

Colchester United,28

Colo-Colo,28

Coventry City,28

Crewe Alexandra,28

Curicó Unido,28

DC United,28

DSC Arminia Bielefeld,28

Daegu FC,28

Dalian YiFang FC,28

Defensa y Justicia,28

Deportes Iquique,28

Deportes Tolima,28

Deportivo Cali,28

Deportivo Pasto,28

Deportivo Toluca,28

Dinamo Zagreb,28

Doncaster Rovers,28

Dynamo Kyiv,28

Eintracht Braunschweig,28

Envigado FC,28

Estudiantes de La Plata,28

Exeter City,28

FC Carl Zeiss Jena,28

FC Energie Cottbus,28

FC Porto,28

FC Seoul,28

FC Sochaux-Montbéliard,28

Feyenoord,28

Fleetwood Town,28

Gangwon FC,28

Getafe CF,28

Gillingham,28

Gimnasia y Esgrima La Plata,28

Godoy Cruz,28

Guangzhou Evergrande Taobao FC,28

Guangzhou R&F; FC,28

Guizhou Hengfeng FC,28

Gyeongnam FC,28

Göztepe SK,28

Hamilton Academical FC,28

Hebei China Fortune FC,28

Henan Jianye FC,28

Incheon United FC,28

Independiente,28

Independiente Medellín,28

Independiente Santa Fe,28

Itagüí Leones FC,28

Jaguares de Córdoba,28

Jeju United FC,28

Jeonbuk Hyundai Motors,28

Jeonnam Dragons,28

Jiangsu Suning FC,28

Junior FC,28

KAA Gent,28

KAS Eupen,28

KFC Uerdingen 05,28

KSV Cercle Brugge,28

KV Kortrijk,28

Karlsruher SC,28

Kashiwa Reysol,28

Kilmarnock,28

La Equidad,28

Lincoln City,28

Livingston FC,28

Lokomotiv Moscow,28

Mansfield Town,28

Medipol Başakşehir FK,28

Millonarios FC,28

Milton Keynes Dons,28

Monarcas Morelia,28

Montpellier HSC,28

Morecambe,28

Motherwell,28

Newell's Old Boys,28

Northampton Town,28

Notts County,28

OGC Nice,28

Olympiacos CFP,28

Once Caldas,28

Orlando Pirates,28

Oxford United,28

PFC CSKA Moscow,28

Panathinaikos FC,28

Patriotas Boyacá FC,28

Patronato,28

Pescara,28

Plymouth Argyle,28

Portsmouth,28

RB Leipzig,28

RC Strasbourg Alsace,28

RCD Mallorca,28

RSC Anderlecht,28

Racing Club,28

Rangers FC,28

Red Star FC,28

Rio Ave FC,28

Rionegro Águilas,28

Rochdale,28

Rosario Central,28

Royal Excel Mouscron,28

SC Braga,28

SG Dynamo Dresden,28

SK Slavia Praha,28

SL Benfica,28

SV Meppen,28

San Lorenzo de Almagro,28

San Luis de Quillota,28

San Martin de Tucumán,28

San Martín de San Juan,28

Sangju Sangmu FC,28

Shakhtar Donetsk,28

Shanghai Greenland Shenhua FC,28

Shanghai SIPG FC,28

Sint-Truidense VV,28

Southend United,28

SpVgg Greuther Fürth,28

Sparta Praha,28

Spezia,28

Sporting Lokeren,28

Sporting de Charleroi,28

Stade Malherbe Caen,28

Standard de Liège,28

Stevenage,28

Sunderland,28

Suwon Samsung Bluewings,28

TSV 1860 München,28

Tianjin TEDA FC,28

Toronto FC,28

Trabzonspor,28

Tranmere Rovers,28

US Salernitana 1919,28

Ulsan Hyundai FC,28

Universidad Católica,28

Universidad de Chile,28

Unión Española,28

Unión de Santa Fe,28

Venezia FC,28

VfL Sportfreunde Lotte,28

Vitesse,28

Vitória de Setúbal,28

Vélez Sarsfield,28

Waasland-Beveren,28

Willem II,28

Yeovil Town,28

 SSV Jahn Regensburg,29

1. FC Nürnberg,29

AD Alcorcón,29

Al Nassr,29

Al Taawoun,29

Amiens SC,29

Atlanta United,29

Cittadella,29

Club Atlas,29

FC Bayern München,29

FC Dallas,29

FC Erzgebirge Aue,29

FC Schalke 04,29

Girona FC,29

Granada CF,29

Guadalajara,29

Hannover 96,29

Hellas Verona,29

Heracles Almelo,29

Hokkaido Consadole Sapporo,29

Holstein Kiel,29

Lecce,29

MKE Ankaragücü,29

Montreal Impact,29

New York Red Bulls,29

Olympique Lyonnais,29

Olympique de Marseille,29

Pachuca,29

Parma,29

Philadelphia Union,29

Preston North End,29

RCD Espanyol,29

SD Eibar,29

SV Sandhausen,29

Stade de Reims,29

Tiburones Rojos de Veracruz,29

U.N.A.M.,29

UD Las Palmas,29

Valenciennes FC,29

Watford,29

AS Nancy Lorraine,30

AZ Alkmaar,30

Ajax,30

Al Ahli,30

Al Batin,30

Al Faisaly,30

Al Hazem,30

Al Hilal,30

Al Ittihad,30

Al Qadisiyah,30

Al Raed,30

Al Shabab,30

Al Wehda,30

Alanyaspor,30

Albacete BP,30

Angers SCO,30

Antalyaspor,30

Ascoli,30

Aston Villa,30

Birmingham City,30

Blackburn Rovers,30

Bolton Wanderers,30

Borussia Mönchengladbach,30

Brentford,30

Brescia,30

Bristol City,30

Bursaspor,30

CD Lugo,30

CD Tenerife,30

Carpi,30

Cerezo Osaka,30

Club América,30

Club León,30

Club Necaxa,30

Cosenza,30

Cádiz CF,30

De Graafschap,30

Deportivo de La Coruña,30

Derby County,30

ESTAC Troyes,30

Ettifaq FC,30

Extremadura UD,30

FC Emmen,30

FC Ingolstadt 04,30

FC Lorient,30

FC St. Pauli,30

FC Tokyo,30

Fenerbahçe SK,30

Galatasaray SK,30

Gamba Osaka,30

Gimnàstic de Tarragona,30

Hamburger SV,30

Houston Dynamo,30

Hull City,30

Ipswich Town,30

Júbilo Iwata,30

Kashima Antlers,30

Kawasaki Frontale,30

Le Havre AC,30

Leeds United,30

Livorno,30

Middlesbrough,30

Millwall,30

Minnesota United FC,30

Málaga CF,30

NAC Breda,30

Norwich City,30

Nottingham Forest,30

Orlando City SC,30

PSV,30

Padova,30

Palermo,30

Paris Saint-Germain,30

Portland Timbers,30

Puebla FC,30

Queens Park Rangers,30

Querétaro,30

Racing Club de Lens,30

Reading,30

Real Oviedo,30

Real Salt Lake,30

Real Sporting de Gijón,30

Real Valladolid CF,30

Real Zaragoza,30

SC Freiburg,30

SC Paderborn 07,30

SD Huesca,30

Sagan Tosu,30

Sevilla FC,30

Sheffield United,30

Sheffield Wednesday,30

Shimizu S-Pulse,30

Shonan Bellmare,30

Sporting CP,30

Stoke City,30

Swansea City,30

Tigres U.A.N.L.,30

UD Almería,30

Udinese,30

V-Varen Nagasaki,30

Vissel Kobe,30

Vitória Guimarães,30

West Bromwich Albion,30

Wigan Athletic,30

Yeni Malatyaspor,30

Yokohama F. Marinos,30

Çaykur Rizespor,30

Athletic Club de Bilbao,31

FC Augsburg,31

FC Girondins de Bordeaux,31

Real Sociedad,31

Toulouse Football Club,31

1. FSV Mainz 05,32

Bournemouth,32

Brighton & Hove Albion,32

Crystal Palace,32

FC Nantes,32

Fulham,32

Hertha BSC,32

Huddersfield Town,32

Lazio,32

Leicester City,32

Levante UD,32

SV Werder Bremen,32

VfL Wolfsburg,32

Villarreal CF,32

West Ham United,32

AS Monaco,33

Arsenal,33

Atlético Madrid,33

Borussia Dortmund,33

Burnley,33

CD Leganés,33

Cardiff City,33

Chelsea,33

Eintracht Frankfurt,33

Empoli,33

Everton,33

FC Barcelona,33

Fortuna Düsseldorf,33

Frosinone,33

Liverpool,33

Manchester City,33

Manchester United,33

Newcastle United,33

RC Celta,33

Rayo Vallecano,33

Real Madrid,33

Southampton,33

TSG 1899 Hoffenheim,33

Tottenham Hotspur,33

Valencia CF,33

Wolverhampton Wanderers,33

None,241

>>> players
           ID                  Name      ...        GKReflexes Release Clause
18206  246269             G. Nugent      ...               9.0          €165K
18202  238813          J. Lundstram      ...               9.0          €143K
18197  246167            D. Holland      ...              15.0           €88K
18195  243582            S. Griffin      ...              13.0          €153K
18196  238477           K. Fujikawa      ...               8.0          €113K
18193  244823            N. Fuentes      ...              11.0           €99K
18188  240927            L. Collins      ...              10.0          €143K
18204  241638             B. Worman      ...              13.0          €165K
18199  244677          M. Baldisimo      ...              15.0          €175K
18205  246268        D. Walker-Rice      ...               9.0          €143K
18198  242844            J. Livesey      ...              48.0          €165K
18200  231381              J. Young      ...              11.0          €143K
18187  240158             C. Ehlich      ...              12.0           €66K
18189  240160            A. Kaltner      ...               8.0          €125K
18192  245571             S. Squire      ...              13.0          €119K
18191  245570  J. Norville-Williams      ...              12.0          €119K
18201  243413              D. Walsh      ...              13.0          €153K
18203  243165    N. Christoffersson      ...              12.0          €113K
18186  240917          Zhang Yufeng      ...               8.0          €167K
18190  245569            L. Watkins      ...               8.0          €165K
18194  245862              J. Milli      ...              44.0          €109K
18173  238520              R. Takae      ...               8.0          €113K
18181  245734              C. Maher      ...              10.0          €109K
18159  244561              L. Jagne      ...              13.0           €98K
18165  245412             H. Norris      ...              11.0          €119K
18169  246446               T. Pugh      ...               6.0          €143K
18156  245533             J. Devine      ...              12.0           €98K
18176  246227            T. Hillman      ...               8.0           €78K
18171  237746           Y. Uchimura      ...              15.0           €25K
18154  243204            M. Roberts      ...               9.0          €143K
...       ...                   ...      ...               ...            ...
27     200145              Casemiro      ...              12.0        €126.4M
38     167664            G. Higuaín      ...              10.0            NaN
34     178603            M. Hummels      ...               6.0         €75.9M
40     162835         S. Handanovič      ...              89.0           €51M
41       1179             G. Buffon      ...              83.0          €7.4M
23     153079             S. Agüero      ...              14.0        €119.3M
14     215914              N. Kanté      ...              10.0        €121.3M
17     194765          A. Griezmann      ...              14.0        €165.8M
15     211110             P. Dybala      ...               8.0        €153.5M
20     189511       Sergio Busquets      ...              13.0        €105.6M
21     179813             E. Cavani      ...              10.0          €111M
18     192448         M. ter Stegen      ...              90.0        €123.3M
24     138956          G. Chiellini      ...               3.0         €44.6M
16     202126               H. Kane      ...              11.0        €160.7M
22     167495              M. Neuer      ...              87.0         €62.7M
19     192119           T. Courtois      ...              88.0        €113.7M
13     168542           David Silva      ...              12.0          €111M
11     182521              T. Kroos      ...              10.0        €156.8M
12     182493              D. Godín      ...              15.0         €90.2M
10     188545        R. Lewandowski      ...              10.0        €127.1M
9      200389              J. Oblak      ...              89.0        €144.5M
6      177003             L. Modrić      ...               9.0        €137.4M
4      192985          K. De Bruyne      ...              13.0        €196.4M
5      183277             E. Hazard      ...               8.0        €172.1M
3      193080                De Gea      ...              94.0        €138.6M
8      155862          Sergio Ramos      ...              11.0        €104.6M
7      176580             L. Suárez      ...              37.0          €164M
2      190871             Neymar Jr      ...              11.0        €228.1M
0      158023              L. Messi      ...               8.0        €226.5M
1       20801     Cristiano Ronaldo      ...              11.0        €127.1M

[18207 rows x 88 columns]
>>> players.stat()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    players.stat()
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\generic.py", line 4376, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'stat'
>>> players.count()
ID                          18207
Name                        18207
Age                         18207
Photo                       18207
Nationality                 18207
Flag                        18207
Overall                     18207
Potential                   18207
Club                        17966
Club Logo                   18207
Value                       18207
Wage                        18207
Special                     18207
Preferred Foot              18159
International Reputation    18159
Weak Foot                   18159
Skill Moves                 18159
Work Rate                   18159
Body Type                   18159
Real Face                   18159
Position                    18147
Jersey Number               18147
Joined                      16654
Loaned From                  1264
Contract Valid Until        17918
Height                      18159
Weight                      18159
LS                          16122
ST                          16122
RS                          16122
                            ...  
Dribbling                   18159
Curve                       18159
FKAccuracy                  18159
LongPassing                 18159
BallControl                 18159
Acceleration                18159
SprintSpeed                 18159
Agility                     18159
Reactions                   18159
Balance                     18159
ShotPower                   18159
Jumping                     18159
Stamina                     18159
Strength                    18159
LongShots                   18159
Aggression                  18159
Interceptions               18159
Positioning                 18159
Vision                      18159
Penalties                   18159
Composure                   18159
Marking                     18159
StandingTackle              18159
SlidingTackle               18159
GKDiving                    18159
GKHandling                  18159
GKKicking                   18159
GKPositioning               18159
GKReflexes                  18159
Release Clause              16643
Length: 88, dtype: int64
>>> players["Preferred Foot"][players["Preferred Foot"]=="Left"].count()
4211
>>> players["Preferred Foot"][players["Preferred Foot"]=="Right"].count()
13948
>>> 4211+13948
18159
>>> players["Preferred Foot"][players["Preferred Foot"]=="NaN"].count()
0
>>> players["Preferred Foot"][players["Preferred Foot"]==""].count()
0
>>> 4211+13948+48
18207
>>> layers["Preferred Foot"][players["ID"]=="221498"].count()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    layers["Preferred Foot"][players["ID"]=="221498"].count()
NameError: name 'layers' is not defined
>>> players["Preferred Foot"][players["ID"]=="221498"].count()

Warning (from warnings module):
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\ops.py", line 1167
    result = method(y)
FutureWarning: elementwise comparison failed; returning scalar instead, but in the future will perform elementwise comparison
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    players["Preferred Foot"][players["ID"]=="221498"].count()
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\ops.py", line 1283, in wrapper
    res = na_op(values, other)
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\ops.py", line 1169, in na_op
    raise TypeError("invalid type comparison")
TypeError: invalid type comparison
>>> players["Preferred Foot"][players["ID"]=="221498"]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    players["Preferred Foot"][players["ID"]=="221498"]
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\ops.py", line 1283, in wrapper
    res = na_op(values, other)
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\ops.py", line 1169, in na_op
    raise TypeError("invalid type comparison")
TypeError: invalid type comparison
>>> players["Preferred Foot"][players["ID"]==221498]
13261    NaN
Name: Preferred Foot, dtype: object
>>> players["Preferred Foot"][players["Preferred Foot"].isna()]
13243    NaN
13261    NaN
13258    NaN
13265    NaN
13276    NaN
13249    NaN
13247    NaN
13238    NaN
13280    NaN
13254    NaN
13242    NaN
13246    NaN
13248    NaN
13257    NaN
13282    NaN
13263    NaN
13274    NaN
13283    NaN
13244    NaN
13253    NaN
13251    NaN
13278    NaN
13266    NaN
13270    NaN
13267    NaN
13272    NaN
13239    NaN
13241    NaN
13245    NaN
13260    NaN
13240    NaN
13273    NaN
13252    NaN
13269    NaN
13275    NaN
13279    NaN
13255    NaN
13256    NaN
13262    NaN
13277    NaN
13237    NaN
13250    NaN
13259    NaN
13264    NaN
13281    NaN
13271    NaN
13236    NaN
13268    NaN
Name: Preferred Foot, dtype: object
>>> y = [18207,4211,13948,48]
>>> x = ["Total","Left Foot","Right Foot","Unknown"]
>>> import pylab as py
>>> py.bar(x,y)
<BarContainer object of 4 artists>
>>> py.title("Prefered Foot")
Text(0.5, 1.0, 'Prefered Foot')
>>> py.show()
>>> y = [
	4211,13948,48]
>>> del x[0]
>>> x
['Left Foot', 'Right Foot', 'Unknown']
>>> py.bar(x,y)
<BarContainer object of 3 artists>
>>> py.title("Prefered Foot")
Text(0.5, 1.0, 'Prefered Foot')
>>> py.show()
>>> y
[4211, 13948, 48]
>>> players["Club"].count()
17966
>>> players["Clube"][players["Clube"].isna]
Traceback (most recent call last):
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\indexes\base.py", line 3078, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 140, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 162, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1492, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1500, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Clube'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    players["Clube"][players["Clube"].isna]
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\frame.py", line 2688, in __getitem__
    return self._getitem_column(key)
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\frame.py", line 2695, in _getitem_column
    return self._get_item_cache(key)
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\generic.py", line 2489, in _get_item_cache
    values = self._data.get(item)
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\internals.py", line 4115, in get
    loc = self.items.get_loc(item)
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\indexes\base.py", line 3080, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 140, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 162, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1492, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1500, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Clube'
>>> players["Clube"][players["Clube"].isna()]
Traceback (most recent call last):
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\indexes\base.py", line 3078, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 140, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 162, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1492, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1500, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Clube'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    players["Clube"][players["Clube"].isna()]
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\frame.py", line 2688, in __getitem__
    return self._getitem_column(key)
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\frame.py", line 2695, in _getitem_column
    return self._get_item_cache(key)
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\generic.py", line 2489, in _get_item_cache
    values = self._data.get(item)
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\internals.py", line 4115, in get
    loc = self.items.get_loc(item)
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\indexes\base.py", line 3080, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 140, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 162, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1492, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1500, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Clube'
>>> players["Club"][players["Clube"].isna()]
Traceback (most recent call last):
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\indexes\base.py", line 3078, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 140, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 162, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1492, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1500, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Clube'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    players["Club"][players["Clube"].isna()]
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\frame.py", line 2688, in __getitem__
    return self._getitem_column(key)
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\frame.py", line 2695, in _getitem_column
    return self._get_item_cache(key)
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\generic.py", line 2489, in _get_item_cache
    values = self._data.get(item)
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\internals.py", line 4115, in get
    loc = self.items.get_loc(item)
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\indexes\base.py", line 3080, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 140, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 162, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1492, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1500, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Clube'
>>> players["Club"][players["Club"].isna()]
17539    NaN
17339    NaN
17436    NaN
17129    NaN
17197    NaN
17215    NaN
16783    NaN
16903    NaN
16793    NaN
16976    NaN
17008    NaN
16947    NaN
16539    NaN
16499    NaN
16450    NaN
15855    NaN
15884    NaN
16265    NaN
16135    NaN
15864    NaN
15652    NaN
15459    NaN
15331    NaN
15393    NaN
15356    NaN
15643    NaN
15825    NaN
15385    NaN
15394    NaN
15762    NaN
        ... 
2399     NaN
2452     NaN
2192     NaN
2259     NaN
2514     NaN
2413     NaN
2289     NaN
2363     NaN
2347     NaN
2080     NaN
1902     NaN
1819     NaN
1933     NaN
1602     NaN
2065     NaN
1964     NaN
1936     NaN
1671     NaN
1907     NaN
1352     NaN
1271     NaN
953      NaN
997      NaN
1008     NaN
1120     NaN
874      NaN
677      NaN
568      NaN
452      NaN
538      NaN
Name: Club, Length: 241, dtype: object
>>> players["Club"][players["Club"].isna()].count()
0
>>> players["Club"][players["Club"]]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    players["Club"][players["Club"]]
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\series.py", line 807, in __getitem__
    if com.is_bool_indexer(key):
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\common.py", line 107, in is_bool_indexer
    raise ValueError('cannot index with vector containing '
ValueError: cannot index with vector containing NA / NaN values
>>> players["Club"][players["Club"].isna()]
		     
17539    NaN
17339    NaN
17436    NaN
17129    NaN
17197    NaN
17215    NaN
16783    NaN
16903    NaN
16793    NaN
16976    NaN
17008    NaN
16947    NaN
16539    NaN
16499    NaN
16450    NaN
15855    NaN
15884    NaN
16265    NaN
16135    NaN
15864    NaN
15652    NaN
15459    NaN
15331    NaN
15393    NaN
15356    NaN
15643    NaN
15825    NaN
15385    NaN
15394    NaN
15762    NaN
        ... 
2399     NaN
2452     NaN
2192     NaN
2259     NaN
2514     NaN
2413     NaN
2289     NaN
2363     NaN
2347     NaN
2080     NaN
1902     NaN
1819     NaN
1933     NaN
1602     NaN
2065     NaN
1964     NaN
1936     NaN
1671     NaN
1907     NaN
1352     NaN
1271     NaN
953      NaN
997      NaN
1008     NaN
1120     NaN
874      NaN
677      NaN
568      NaN
452      NaN
538      NaN
Name: Club, Length: 241, dtype: object
>>> players["Club"][!players["Club"].isna()]
		     
SyntaxError: invalid syntax
>>> players["Club"][players["Club"].isna()==False]
		     
18206               Tranmere Rovers
18202               Crewe Alexandra
18197                     Cork City
18195                  Waterford FC
18196                  Júbilo Iwata
18193                Unión Española
18188                Newport County
18204              Cambridge United
18199        Vancouver Whitecaps FC
18205               Tranmere Rovers
18198                 Burton Albion
18200                  Swindon Town
18187            SpVgg Unterhaching
18189            SpVgg Unterhaching
18192              Cambridge United
18191              Cambridge United
18201                  Waterford FC
18203                Trelleborgs FF
18186              Beijing Renhe FC
18190              Cambridge United
18194                         Lecce
18173                   Gamba Osaka
18181                Bray Wanderers
18159                     Morecambe
18165               Oldham Athletic
18169             Scunthorpe United
18156               Tranmere Rovers
18176                Newport County
18171    Hokkaido Consadole Sapporo
18154              Northampton Town
                    ...            
27                      Real Madrid
38                            Milan
34                FC Bayern München
40                            Inter
41              Paris Saint-Germain
23                  Manchester City
14                          Chelsea
17                  Atlético Madrid
15                         Juventus
20                     FC Barcelona
21              Paris Saint-Germain
18                     FC Barcelona
24                         Juventus
16                Tottenham Hotspur
22                FC Bayern München
19                      Real Madrid
13                  Manchester City
11                      Real Madrid
12                  Atlético Madrid
10                FC Bayern München
9                   Atlético Madrid
6                       Real Madrid
4                   Manchester City
5                           Chelsea
3                 Manchester United
8                       Real Madrid
7                      FC Barcelona
2               Paris Saint-Germain
0                      FC Barcelona
1                          Juventus
Name: Club, Length: 17966, dtype: object
>>> players["Club"].unique()
		     
array(['Tranmere Rovers', 'Crewe Alexandra', 'Cork City', 'Waterford FC',
       'Júbilo Iwata', 'Unión Española', 'Newport County',
       'Cambridge United', 'Vancouver Whitecaps FC', 'Burton Albion',
       'Swindon Town', 'SpVgg Unterhaching', 'Trelleborgs FF',
       'Beijing Renhe FC', 'Lecce', 'Gamba Osaka', 'Bray Wanderers',
       'Morecambe', 'Oldham Athletic', 'Scunthorpe United',
       'Hokkaido Consadole Sapporo', 'Northampton Town', 'Örebro SK',
       'Shrewsbury', 'New England Revolution', 'Vejle Boldklub',
       'Fleetwood Town', 'Guangzhou R&F; FC', 'Derry City',
       "St. Patrick's Athletic", 'Tianjin Quanjian FC', 'Carlisle United',
       'Blackpool', 'Atlético Nacional', 'Odense Boldklub',
       'Beijing Sinobo Guoan FC', 'St. Johnstone FC', 'Dalkurd FF',
       'Wisła Płock', 'Lincoln City', 'LASK Linz', 'CD Huachipato',
       'Hamilton Academical FC', 'Tianjin TEDA FC', 'Luton Town',
       'Sligo Rovers', 'SønderjyskE',
       'Chongqing Dangdai Lifan FC SWM Team', 'Grimsby Town',
       'Bohemian FC', 'Limerick FC', 'Jiangsu Suning FC',
       'FC Nordsjælland', 'Stevenage', 'Perugia', 'Barnsley', 'SV Meppen',
       'Shanghai SIPG FC', 'Kilmarnock', 'Crotone',
       'FC Würzburger Kickers', 'GIF Sundsvall', 'Al Batin', 'Aberdeen',
       'Charlton Athletic', 'Brøndby IF', 'Ascoli', 'Guizhou Hengfeng FC',
       'Stabæk Fotball', 'Atlético Huila', 'Kashiwa Reysol', 'Port Vale',
       'Al Taawoun', 'Esbjerg fB', 'HJK Helsinki', 'TSV Hartberg',
       'Sandefjord Fotball', 'Al Raed', 'Milton Keynes Dons',
       'Vålerenga Fotball', 'Sanfrecce Hiroshima', 'Melbourne Victory',
       'IFK Göteborg', 'San Luis de Quillota', 'Doncaster Rovers',
       'Crawley Town', 'Aalborg BK', 'Pohang Steelers', 'América de Cali',
       'Hobro IK', 'Santos Laguna', 'Western Sydney Wanderers',
       'Changchun Yatai FC', 'FC Thun', 'Zagłębie Lubin', 'BK Häcken',
       'IFK Norrköping', 'Östersunds FK', 'Independiente Medellín',
       'Shamrock Rovers', 'Deportivo Toluca', 'TSV 1860 München',
       'Jagiellonia Białystok', 'SK Slavia Praha', 'BB Erzurumspor',
       'FC Midtjylland', 'Al Nassr', 'Tiburones Rojos de Veracruz',
       'AC Horsens', 'Yokohama F. Marinos', 'Göztepe SK',
       'Stade Malherbe Caen', 'Shanghai Greenland Shenhua FC',
       'Beşiktaş JK', 'SV Darmstadt 98', 'Exeter City', 'Gyeongnam FC',
       'Watford', 'Guangzhou Evergrande Taobao FC', 'FK Bodø/Glimt',
       'SKN St. Pölten', 'Shandong Luneng TaiShan FC', 'Wisła Kraków',
       'Oxford United', 'Daegu FC', 'FC Sochaux-Montbéliard',
       'Motherwell', 'Sporting de Charleroi', 'Hibernian',
       'Miedź Legnica', 'St. Mirren', 'Adelaide United',
       'Henan Jianye FC', 'Odds BK', 'Zagłębie Sosnowiec',
       'Vendsyssel FF', 'AFC Wimbledon', 'Foggia', 'Toronto FC',
       'FC St. Gallen', 'Envigado FC', 'Wolfsberger AC',
       'Preston North End', 'Jeju United FC', 'Melbourne City FC',
       'Aarhus GF', 'Malmö FF', 'Independiente Santa Fe',
       'Grasshopper Club Zürich', 'Dundalk', 'Dalian YiFang FC',
       'Al Fateh', 'SC Paderborn 07', 'Plymouth Argyle',
       'Boyacá Chicó FC', 'Curicó Unido', 'Gillingham', 'Audax Italiano',
       'Argentinos Juniors', 'SC Preußen Münster', 'Molde FK',
       'FC Dallas', 'Randers FC', 'Coventry City', 'Lechia Gdańsk',
       'SK Brann', 'KFC Uerdingen 05', 'Houston Dynamo',
       'New York City FC', 'SPAL', 'Korona Kielce', 'Orlando Pirates',
       'Kashima Antlers', 'Dynamo Kyiv', 'Sheffield Wednesday',
       'Club Atlético Tigre', 'CD Antofagasta', 'V-Varen Nagasaki',
       'Vissel Kobe', 'Ohod Club', 'Dundee FC', 'Sydney FC',
       'Sarpsborg 08 FF', "CD O'Higgins", 'Livorno', 'FC Ingolstadt 04',
       'FC Zürich', 'Accrington Stanley', 'Rosenborg BK', 'Carpi',
       'FC Admira Wacker Mödling', 'Livingston FC', 'Unión La Calera',
       'SK Sturm Graz', 'Wellington Phoenix', 'Yeovil Town',
       'VfL Osnabrück', 'Hammarby IF', 'Empoli', 'Cardiff City',
       'Bristol City', 'IK Sirius', 'La Berrichonne de Châteauroux',
       'Notts County', 'Tromsø IL', 'Djurgårdens IF', 'Macclesfield Town',
       'Al Shabab', 'Portsmouth', 'Kasimpaşa SK', 'Bristol Rovers',
       'Sheffield United', 'Kalmar FF', 'Cerezo Osaka', 'Shonan Bellmare',
       'MSV Duisburg', ' SSV Jahn Regensburg', 'Al Ahli',
       'Valenciennes FC', 'Sivasspor', 'Jaguares de Córdoba', 'Walsall',
       'Central Coast Mariners', 'GFC Ajaccio', 'Lillestrøm SK',
       'Karlsruher SC', 'Millwall', 'FC Erzgebirge Aue', 'Nagoya Grampus',
       'Universidad Católica', 'Deportes Tolima', 'Cheltenham Town',
       'Aston Villa', 'Arka Gdynia', 'Urawa Red Diamonds', 'Santa Clara',
       '1. FC Heidenheim 1846', 'FC Carl Zeiss Jena', 'Perth Glory',
       'FC Luzern', 'AIK', 'Sint-Truidense VV', 'Deportivo Pasto',
       'SC Fortuna Köln', 'Górnik Zabrze', 'Incheon United FC',
       'AC Ajaccio', 'FK Haugesund', 'FC Lugano', 'Portland Timbers',
       'Patronato', 'RC Strasbourg Alsace', 'Hallescher FC', 'Cracovia',
       'FC Basel 1893', 'FC Tokyo', 'US Salernitana 1919',
       'Neuchâtel Xamax', 'VfR Aalen', 'IF Elfsborg',
       'Philadelphia Union', nan, 'Bradford City', 'Colchester United',
       'FC Lorient', '1. FC Köln', 'Śląsk Wrocław', 'Deportes Iquique',
       'Vegalta Sendai', '1. FC Union Berlin', 'Derby County',
       'Sunderland', 'Bury', 'Alianza Petrolera', 'Club Tijuana',
       'Brisbane Roar', 'Patriotas Boyacá FC', 'Middlesbrough', 'FC Sion',
       'SG Sonnenhof Großaspach', 'Club Deportes Temuco',
       'Itagüí Leones FC', 'FC Energie Cottbus', 'US Cremonese',
       'CD Palestino', 'SD Huesca', 'Wigan Athletic', 'Ipswich Town',
       'Kristiansund BK', 'FC Wacker Innsbruck', 'AEK Athens',
       'Stade de Reims', 'Brighton & Hove Albion', 'Venezia FC',
       'Queens Park Rangers', 'Hebei China Fortune FC',
       'Yeni Malatyaspor', 'Atlanta United', 'Mansfield Town',
       'BSC Young Boys', 'SG Dynamo Dresden', 'Willem II',
       'Wolverhampton Wanderers', 'CD Everton de Viña del Mar',
       'Al Hazem', 'Bolton Wanderers', 'Spezia', 'FC Hansa Rostock',
       'Birmingham City', 'Hull City', 'Belgrano de Córdoba',
       'IF Brommapojkarna', 'Piast Gliwice', 'De Graafschap',
       'Monarcas Morelia', 'Once Caldas', 'Pogoń Szczecin',
       'VfL Bochum 1848', 'Manchester City', 'Sagan Tosu',
       'Newcastle Jets', 'Atlético Bucaramanga', 'Al Qadisiyah', 'Fulham',
       'Gimnasia y Esgrima La Plata', 'SCR Altach', 'Rangers FC',
       'FC København', '1. FC Kaiserslautern', 'Montreal Impact',
       'Kawasaki Frontale', 'Le Havre AC', 'Monterrey', 'Shimizu S-Pulse',
       'Al Wehda', 'Querétaro', 'FK Austria Wien', 'Burnley',
       'Al Faisaly', 'Benevento', 'Colo-Colo', 'Crystal Palace',
       'Rotherham United', 'FC Emmen', 'Club Atlético Colón',
       'Racing Club de Lens', 'Colorado Rapids', 'AS Nancy Lorraine',
       'Blackburn Rovers', 'RCD Espanyol', 'Racing Club',
       'US Orléans Loiret Football', 'Chamois Niortais Football Club',
       'Girona FC', 'Kayserispor', 'Ettifaq FC', 'Sangju Sangmu FC',
       'Ranheim Fotball', 'Pachuca', 'River Plate', 'Forest Green Rovers',
       'Vélez Sarsfield', 'Norwich City', 'Huddersfield Town',
       'Orlando City SC', 'Rochdale', 'Lech Poznań', 'Newcastle United',
       'Cádiz CF', 'Universidad de Chile', 'Peterborough United',
       'Sassuolo', 'Strømsgodset IF', 'Al Fayha', 'Cosenza', 'Sampdoria',
       'AS Béziers', 'Leeds United', 'CD Numancia', 'Al Ittihad',
       'SK Rapid Wien', 'Holstein Kiel', 'Minnesota United FC',
       'Sporting Lokeren', 'Real Salt Lake', 'Antalyaspor',
       'Medipol Başakşehir FK', 'Southend United', 'Gangwon FC',
       'La Equidad', 'Club Atlas', 'Kaizer Chiefs', 'VVV-Venlo',
       'Çaykur Rizespor', 'FC St. Pauli', 'Excelsior',
       'CD Universidad de Concepción', 'Al Hilal', 'Cruz Azul',
       'FC Groningen', 'Heart of Midlothian', 'Clermont Foot 63',
       'Rionegro Águilas', 'Alanyaspor', 'VfL Sportfreunde Lotte',
       'Real Valladolid CF', 'AJ Auxerre', 'Albacete BP',
       'AS Saint-Étienne', 'Estudiantes de La Plata', 'Brentford',
       'Legia Warszawa', 'SV Mattersburg', 'KAS Eupen',
       'New York Red Bulls', '1. FC Magdeburg', 'Rosario Central',
       'Fortuna Sittard', 'San Jose Earthquakes',
       'Eintracht Braunschweig', 'FC Bayern München', 'FC Augsburg',
       'Chelsea', 'Los Angeles FC', 'Royal Excel Mouscron', 'Bournemouth',
       'U.N.A.M.', 'West Ham United', 'Heracles Almelo',
       'Club Atlético Talleres', 'Real Sociedad', 'Puebla FC',
       'Club León', 'Vitesse', 'FC Red Bull Salzburg',
       'Club Atlético Huracán', 'NAC Breda', 'Frosinone', 'RB Leipzig',
       'Wycombe Wanderers', 'Fiorentina', 'Deportivo Cali',
       'Lokomotiv Moscow', 'Jeonnam Dragons', 'Godoy Cruz',
       "Newell's Old Boys", 'Real Betis', 'Palermo', 'PEC Zwolle',
       'MKE Ankaragücü', 'Fortuna Düsseldorf', 'Pescara', 'Paris FC',
       'Seattle Sounders FC', 'Boavista FC', 'Jeonbuk Hyundai Motors',
       'FC Schalke 04', 'Nîmes Olympique', 'Lobos BUAP', 'Dijon FCO',
       'Rayo Vallecano', 'Unión de Santa Fe', 'Junior FC',
       'Borussia Dortmund', 'KV Kortrijk', 'LA Galaxy',
       'Atlético Tucumán', 'Galatasaray SK', 'TSG 1899 Hoffenheim',
       'Nottingham Forest', 'Club Necaxa', '1. FSV Mainz 05',
       'DSC Arminia Bielefeld', 'San Martin de Tucumán', 'Hannover 96',
       'Amiens SC', 'Stade Brestois 29', 'Angers SCO', 'Elche CF',
       'IK Start', 'PAOK', 'Cittadella', 'Olympique de Marseille',
       'Arsenal', 'SC Freiburg', 'Bursaspor', 'CD Lugo', 'FSV Zwickau',
       'Club Atlético Aldosivi', 'Hellas Verona', 'SpVgg Greuther Fürth',
       'Córdoba CF', 'PFC CSKA Moscow', 'Sparta Praha',
       'Columbus Crew SC', 'Guadalajara', 'FC Utrecht',
       'SV Zulte-Waregem', 'Viktoria Plzeň', 'Suwon Samsung Bluewings',
       'SV Wehen Wiesbaden', 'Sporting Kansas City', 'KSV Cercle Brugge',
       'Hertha BSC', 'Club Atlético Banfield', 'Millonarios FC',
       'Atlético Madrid', 'Montpellier HSC', 'Liverpool',
       'CF Reus Deportiu', 'UD Almería', '1. FC Nürnberg',
       'Defensa y Justicia', 'Red Star FC', 'Eintracht Frankfurt',
       'Bayer 04 Leverkusen', 'ADO Den Haag', 'Grenoble Foot 38',
       'VfB Stuttgart', 'Málaga CF', 'VfL Wolfsburg', 'LOSC Lille',
       'Swansea City', 'Feyenoord', 'SV Werder Bremen', 'KV Oostende',
       'CD Leganés', 'Chicago Fire', 'Southampton', 'Club América',
       'Borussia Mönchengladbach', 'Dinamo Zagreb', 'Torino',
       'Toulouse Football Club', 'FC Girondins de Bordeaux',
       'Olympique Lyonnais', 'Everton', 'Ulsan Hyundai FC',
       'ESTAC Troyes', 'Waasland-Beveren', 'Athletic Club de Bilbao',
       'SC Heerenveen', 'SD Eibar', 'FC Seoul', 'Club Brugge KV',
       'Brescia', 'DC United', 'Reading', 'Panathinaikos FC',
       'Real Zaragoza', 'West Bromwich Albion', 'Standard de Liège',
       'Club Atlético Lanús', 'Hamburger SV', 'Lazio',
       'San Lorenzo de Almagro', 'Tigres U.A.N.L.', 'Stade Rennais FC',
       'Genoa', 'AD Alcorcón', 'Independiente', 'Chievo Verona',
       'Boca Juniors', 'Extremadura UD', 'Stoke City',
       'En Avant de Guingamp', 'CD Tenerife', 'RCD Mallorca', 'Bologna',
       'Padova', 'Getafe CF', 'Granada CF', 'PSV', 'CF Rayo Majadahonda',
       'Atalanta', 'Real Sporting de Gijón', 'Real Oviedo',
       'Tottenham Hotspur', 'CA Osasuna', 'SV Sandhausen', 'Trabzonspor',
       'FC Nantes', 'Deportivo Alavés', 'RC Celta', 'Sevilla FC',
       'KAA Gent', 'Valencia CF', 'San Martín de San Juan',
       'Royal Antwerp FC', 'UD Las Palmas', 'Villarreal CF',
       'Akhisar Belediyespor', 'FC Barcelona', 'OGC Nice',
       'Gimnàstic de Tarragona', 'FC Metz', 'Shakhtar Donetsk',
       'RSC Anderlecht', 'AS Monaco', 'Portimonense SC',
       'Sport Club do Recife', 'Vitória de Setúbal', 'Atiker Konyaspor',
       'Leicester City', 'Santos', 'Moreirense FC', 'Fenerbahçe SK',
       'CD Nacional', 'Real Madrid', 'Juventus', 'Ceará Sporting Club',
       'Paris Saint-Germain', 'Levante UD', 'CD Tondela', 'Celtic',
       'Deportivo de La Coruña', 'CD Feirense', 'Sporting CP',
       'Rio Ave FC', 'AZ Alkmaar', 'Vitória', 'Manchester United',
       'Parma', 'Paraná', 'Chapecoense', 'Atlético Paranaense',
       'Os Belenenses', 'GD Chaves', 'CD Aves',
       'América FC (Minas Gerais)', 'Bahia', 'Spartak Moscow', 'KRC Genk',
       'Inter', 'Roma', 'Ajax', 'Grêmio', 'Udinese', 'Vitória Guimarães',
       'Fluminense', 'Clube Sport Marítimo', 'Botafogo', 'Cruzeiro',
       'Milan', 'SC Braga', 'Cagliari', 'FC Porto', 'Internacional',
       'Atlético Mineiro', 'SL Benfica', 'Olympiacos CFP', 'Napoli'],
      dtype=object)
>>> [players["Club"].isna().count()
     ]
		     
[18207]
>>> players["Club"].unique().count()
		     
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    players["Club"].unique().count()
AttributeError: 'numpy.ndarray' object has no attribute 'count'
>>> [players["Club"].unique()].count()
		     
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    [players["Club"].unique()].count()
TypeError: count() takes exactly one argument (0 given)
>>> len(players["Club"].unique())
		     
652
>>> players["Club"].unique().count()
		     
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    players["Club"].unique().count()
AttributeError: 'numpy.ndarray' object has no attribute 'count'
>>> 
		     
>>> 241+17966
		     
18207
>>> players["Club"][players["Club"].isna()].count()
		     
0
>>> len(players["Club"][players["Club"].isna()])
		     
241
>>> x = [17966,241]
		     
>>> y = x
		     
>>> x = ["Joined Club","Don't joined Club"]
		     
>>> py
		     
<module 'pylab' from 'C:\\Users\\Hp\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\site-packages\\pylab.py'>
>>> py.pie(y,autopct="%.2f",labels=x)
		     
([<matplotlib.patches.Wedge object at 0x0E54B4B0>, <matplotlib.patches.Wedge object at 0x0E54B8F0>], [Text(-1.099049054803289, 0.04572936841896313, 'Joined Club'), Text(1.0990490584157948, -0.045729281596751846, "Don't joined Club")], [Text(-0.5994813026199757, 0.024943291864888976, '98.68'), Text(0.5994813045904335, -0.024943244507319186, '1.32')])
>>> py.title("Player participation in club")
		     
Text(0.5, 1.0, 'Player participation in club')
>>> py.show()
		     
>>> x
		     
['Joined Club', "Don't joined Club"]
>>> y
		     
[17966, 241]
>>> py.pie(y,autopct="{.2f}%",labels=x)
		     
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    py.pie(y,autopct="{.2f}%",labels=x)
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\matplotlib\pyplot.py", line 2805, in pie
    data is not None else {}))
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\matplotlib\__init__.py", line 1810, in inner
    return func(ax, *args, **kwargs)
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\matplotlib\axes\_axes.py", line 2890, in pie
    s = autopct % (100. * frac)
ValueError: incomplete format
>>> py.pie(y,autopct="{%.2f}%",labels=x)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    py.pie(y,autopct="{%.2f}%",labels=x)
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\matplotlib\pyplot.py", line 2805, in pie
    data is not None else {}))
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\matplotlib\__init__.py", line 1810, in inner
    return func(ax, *args, **kwargs)
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\matplotlib\axes\_axes.py", line 2890, in pie
    s = autopct % (100. * frac)
ValueError: incomplete format
>>> py.pie(y,autopct="{p:.2f}%",labels=x)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    py.pie(y,autopct="{p:.2f}%",labels=x)
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\matplotlib\pyplot.py", line 2805, in pie
    data is not None else {}))
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\matplotlib\__init__.py", line 1810, in inner
    return func(ax, *args, **kwargs)
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\matplotlib\axes\_axes.py", line 2890, in pie
    s = autopct % (100. * frac)
ValueError: incomplete format
>>> py.pie(y,autopct='{p:.2f}',labels=x)
([<matplotlib.patches.Wedge object at 0x0EDEE450>, <matplotlib.patches.Wedge object at 0x0EDEE870>], [Text(-1.099049054803289, 0.04572936841896313, 'Joined Club'), Text(1.0990490584157948, -0.045729281596751846, "Don't joined Club")], [Text(-0.5994813026199757, 0.024943291864888976, '{p:.2f}'), Text(0.5994813045904335, -0.024943244507319186, '{p:.2f}')])
>>> py.show()
>>> py.pie(y,autopct="{p:%.2f}%",labels=x)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    py.pie(y,autopct="{p:%.2f}%",labels=x)
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\matplotlib\pyplot.py", line 2805, in pie
    data is not None else {}))
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\matplotlib\__init__.py", line 1810, in inner
    return func(ax, *args, **kwargs)
  File "C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\matplotlib\axes\_axes.py", line 2890, in pie
    s = autopct % (100. * frac)
ValueError: incomplete format
>>> py.pie(y,autopct="{p:%.2f}",labels=x)
([<matplotlib.patches.Wedge object at 0x0EDD06F0>, <matplotlib.patches.Wedge object at 0x0EDD0AD0>], [Text(-1.099049054803289, 0.04572936841896313, 'Joined Club'), Text(1.0990490584157948, -0.045729281596751846, "Don't joined Club")], [Text(-0.5994813026199757, 0.024943291864888976, '{p:98.68}'), Text(0.5994813045904335, -0.024943244507319186, '{p:1.32}')])
>>> py.show()
>>> py.pie(y,autopct="%.2f%%",labels=x)
([<matplotlib.patches.Wedge object at 0x0F37C6D0>, <matplotlib.patches.Wedge object at 0x0F37CB10>], [Text(-1.099049054803289, 0.04572936841896313, 'Joined Club'), Text(1.0990490584157948, -0.045729281596751846, "Don't joined Club")], [Text(-0.5994813026199757, 0.024943291864888976, '98.68%'), Text(0.5994813045904335, -0.024943244507319186, '1.32%')])
>>> py.show()
>>> players["Age"]

>>> list(players["Age"])
[16, 19, 18, 18, 19, 18, 17, 16, 18, 17, 18, 18, 19, 18, 18, 18, 18, 19, 20, 18, 18, 20, 17, 20, 17, 17, 18, 17, 33, 17, 16, 17, 17, 16, 19, 20, 19, 19, 21, 18, 18, 17, 18, 18, 18, 18, 22, 18, 18, 18, 18, 18, 44, 18, 20, 19, 20, 18, 19, 16, 18, 17, 19, 20, 18, 17, 19, 20, 18, 17, 19, 17, 20, 17, 21, 18, 20, 19, 17, 17, 19, 18, 18, 18, 18, 19, 21, 17, 17, 18, 19, 18, 21, 17, 26, 20, 18, 17, 18, 19, 21, 21, 18, 20, 16, 19, 18, 19, 18, 17, 21, 18, 17, 17, 17, 19, 18, 20, 17, 17, 19, 17, 18, 17, 18, 19, 17, 18, 20, 18, 18, 19, 19, 21, 21, 21, 16, 19, 18, 20, 18, 18, 20, 19, 24, 18, 16, 17, 23, 18, 26, 20, 19, 18, 24, 17, 17, 18, 19, 19, 22, 19, 27, 17, 20, 18, 18, 24, 20, 18, 27, 17, 20, 21, 19, 18, 17, 19, 19, 31, 17, 20, 26, 19, 18, 20, 17, 21, 21, 18, 17, 19, 19, 25, 17, 17, 19, 22, 19, 18, 18, 20, 17, 21, 21, 16, 19, 18, 20, 23, 18, 19, 22, 17, 17, 19, 19, 19, 19, 18, 19, 16, 20, 19, 17, 21, 18, 16, 19, 18, 21, 17, 20, 19, 20, 17, 18, 23, 17, 17, 18, 23, 19, 17, 20, 19, 18, 17, 17, 18, 17, 21, 18, 18, 17, 19, 18, 19, 20, 19, 19, 18, 17, 20, 22, 18, 18, 21, 21, 18, 18, 21, 18, 18, 17, 22, 19, 20, 18, 18, 19, 17, 20, 19, 21, 18, 22, 19, 18, 17, 18, 21, 28, 19, 19, 19, 20, 18, 17, 18, 19, 17, 21, 24, 19, 19, 20, 22, 18, 19, 19, 17, 19, 22, 20, 18, 20, 17, 19, 16, 21, 18, 17, 20, 21, 17, 21, 17, 19, 18, 17, 19, 19, 20, 16, 18, 19, 18, 18, 22, 17, 18, 19, 21, 18, 16, 20, 21, 19, 18, 22, 16, 22, 19, 18, 21, 19, 18, 21, 20, 23, 18, 19, 19, 18, 18, 19, 18, 21, 18, 17, 22, 24, 21, 16, 19, 21, 20, 16, 25, 19, 18, 16, 17, 21, 20, 23, 20, 21, 18, 20, 16, 19, 18, 20, 19, 18, 19, 19, 18, 17, 19, 17, 19, 20, 21, 20, 39, 22, 17, 16, 21, 18, 19, 28, 40, 21, 19, 17, 18, 19, 17, 19, 21, 23, 18, 20, 32, 20, 18, 19, 19, 18, 20, 17, 30, 21, 17, 23, 20, 19, 18, 19, 21, 19, 18, 22, 21, 23, 21, 21, 17, 18, 19, 21, 19, 17, 18, 19, 19, 23, 30, 19, 18, 20, 18, 21, 22, 19, 19, 19, 21, 21, 23, 20, 18, 19, 19, 19, 21, 19, 17, 19, 19, 18, 18, 19, 20, 22, 21, 17, 21, 17, 19, 17, 18, 18, 18, 18, 19, 17, 19, 18, 20, 19, 17, 18, 19, 19, 18, 18, 22, 25, 22, 18, 20, 17, 20, 22, 18, 18, 19, 17, 19, 19, 19, 19, 20, 17, 18, 23, 21, 18, 19, 19, 18, 19, 22, 22, 18, 23, 21, 19, 21, 19, 23, 21, 18, 19, 18, 19, 19, 18, 21, 18, 20, 17, 17, 18, 21, 20, 20, 19, 21, 19, 20, 20, 23, 21, 20, 21, 19, 19, 22, 18, 21, 19, 18, 18, 21, 20, 21, 19, 20, 18, 19, 21, 20, 19, 17, 19, 22, 22, 21, 26, 19, 23, 18, 18, 39, 25, 23, 19, 24, 19, 23, 18, 21, 19, 19, 19, 19, 18, 21, 20, 18, 24, 19, 22, 27, 20, 20, 19, 19, 20, 18, 24, 36, 20, 19, 18, 19, 17, 18, 20, 18, 23, 21, 35, 20, 24, 20, 21, 17, 21, 20, 20, 21, 19, 18, 20, 19, 17, 17, 18, 19, 20, 22, 17, 18, 20, 19, 24, 44, 20, 18, 16, 21, 23, 29, 19, 18, 18, 21, 25, 18, 17, 20, 19, 18, 21, 18, 20, 19, 17, 20, 23, 20, 19, 21, 20, 18, 24, 20, 18, 17, 22, 21, 28, 18, 21, 18, 20, 19, 19, 17, 21, 17, 20, 23, 20, 18, 19, 20, 20, 19, 18, 19, 17, 21, 21, 18, 21, 18, 21, 18, 19, 18, 22, 18, 19, 18, 19, 19, 18, 22, 20, 19, 18, 21, 19, 18, 18, 21, 20, 17, 17, 19, 18, 20, 19, 18, 19, 20, 18, 21, 18, 25, 21, 17, 21, 18, 17, 17, 18, 22, 19, 16, 19, 20, 18, 18, 21, 22, 21, 18, 19, 18, 24, 19, 20, 19, 19, 17, 18, 19, 17, 22, 23, 19, 21, 19, 21, 17, 17, 20, 18, 17, 19, 18, 20, 19, 19, 21, 22, 20, 21, 18, 21, 25, 19, 19, 18, 20, 18, 21, 17, 21, 21, 21, 19, 18, 19, 21, 20, 18, 19, 19, 18, 21, 18, 18, 18, 21, 17, 18, 17, 18, 20, 26, 21, 22, 18, 17, 17, 20, 18, 21, 18, 19, 19, 18, 19, 18, 19, 20, 19, 22, 19, 23, 38, 17, 20, 19, 23, 17, 18, 19, 21, 21, 20, 18, 23, 19, 20, 22, 20, 18, 20, 20, 17, 20, 19, 23, 21, 18, 19, 19, 34, 18, 29, 18, 20, 23, 21, 20, 19, 19, 25, 20, 19, 19, 22, 20, 22, 19, 17, 26, 21, 18, 21, 21, 20, 19, 23, 18, 23, 24, 20, 19, 23, 17, 35, 21, 25, 23, 18, 18, 16, 18, 20, 22, 18, 18, 26, 17, 18, 21, 19, 21, 19, 21, 21, 18, 19, 19, 21, 20, 21, 18, 20, 19, 25, 16, 18, 18, 20, 18, 18, 19, 19, 20, 27, 19, 19, 20, 21, 19, 18, 18, 21, 19, 22, 18, 18, 20, 16, 18, 22, 19, 19, 18, 21, 17, 17, 21, 28, 18, 23, 16, 18, 18, 18, 18, 19, 20, 19, 22, 19, 17, 20, 19, 19, 20, 16, 17, 18, 16, 18, 19, 18, 18, 18, 25, 19, 20, 19, 17, 21, 18, 23, 20, 23, 21, 19, 22, 17, 18, 18, 22, 20, 20, 19, 18, 25, 19, 25, 26, 25, 21, 25, 19, 21, 24, 18, 20, 19, 18, 22, 20, 22, 19, 20, 19, 19, 17, 20, 20, 24, 29, 19, 18, 24, 21, 28, 21, 22, 18, 18, 21, 22, 20, 20, 23, 18, 19, 24, 20, 19, 18, 20, 23, 19, 23, 19, 21, 19, 20, 19, 19, 19, 19, 18, 21, 21, 20, 22, 21, 19, 17, 21, 19, 20, 18, 19, 25, 22, 19, 19, 20, 18, 23, 29, 18, 22, 18, 20, 19, 17, 20, 22, 21, 27, 24, 18, 31, 23, 37, 20, 29, 23, 30, 19, 21, 19, 19, 19, 22, 24, 20, 19, 21, 19, 21, 17, 18, 20, 18, 28, 17, 21, 19, 21, 23, 18, 18, 23, 26, 22, 25, 21, 22, 21, 24, 21, 25, 29, 22, 29, 21, 27, 21, 25, 20, 23, 22, 26, 18, 23, 34, 18, 18, 20, 17, 23, 20, 23, 22, 20, 25, 19, 17, 19, 20, 19, 20, 20, 21, 19, 20, 20, 19, 24, 19, 22, 19, 20, 20, 18, 21, 19, 19, 25, 20, 19, 19, 20, 21, 17, 23, 20, 17, 22, 19, 20, 19, 21, 18, 19, 19, 23, 23, 23, 18, 19, 19, 20, 20, 24, 19, 19, 21, 18, 26, 18, 20, 18, 18, 23, 18, 19, 17, 21, 19, 19, 20, 18, 18, 18, 26, 18, 17, 18, 20, 18, 19, 20, 20, 21, 21, 18, 19, 19, 31, 20, 18, 23, 21, 20, 17, 19, 19, 20, 21, 20, 17, 18, 23, 18, 18, 18, 21, 20, 21, 19, 21, 18, 22, 18, 22, 20, 19, 20, 24, 21, 21, 19, 17, 24, 22, 23, 18, 23, 21, 21, 20, 19, 23, 22, 20, 18, 18, 19, 19, 19, 20, 24, 20, 28, 19, 26, 21, 19, 17, 20, 19, 17, 21, 18, 18, 18, 20, 21, 21, 23, 23, 22, 22, 23, 23, 21, 20, 23, 19, 21, 23, 17, 19, 19, 20, 22, 19, 21, 20, 16, 24, 19, 19, 21, 19, 19, 24, 18, 24, 22, 20, 24, 20, 23, 21, 18, 20, 19, 28, 27, 22, 21, 20, 20, 22, 18, 20, 22, 23, 19, 22, 21, 19, 20, 20, 19, 23, 22, 23, 21, 30, 25, 26, 22, 20, 19, 18, 18, 21, 18, 21, 18, 24, 22, 19, 20, 19, 21, 28, 35, 20, 18, 22, 17, 18, 21, 21, 18, 18, 21, 21, 19, 20, 23, 34, 20, 20, 21, 19, 26, 19, 20, 22, 26, 19, 23, 21, 24, 20, 29, 26, 22, 26, 18, 19, 21, 18, 17, 18, 23, 17, 22, 20, 19, 20, 23, 19, 24, 20, 21, 21, 35, 18, 21, 23, 22, 21, 21, 19, 20, 21, 26, 23, 21, 23, 31, 18, 20, 22, 19, 19, 19, 26, 24, 31, 23, 19, 21, 19, 20, 18, 20, 25, 18, 19, 17, 19, 20, 18, 19, 23, 17, 20, 18, 28, 20, 22, 23, 21, 32, 25, 19, 29, 20, 20, 24, 18, 26, 20, 18, 22, 20, 20, 22, 19, 18, 21, 18, 17, 21, 19, 20, 19, 22, 21, 20, 18, 19, 20, 18, 20, 24, 17, 21, 20, 19, 22, 19, 21, 27, 18, 19, 21, 22, 19, 22, 19, 18, 25, 19, 20, 21, 18, 18, 20, 20, 23, 18, 18, 20, 18, 18, 21, 21, 18, 20, 18, 16, 18, 18, 20, 20, 21, 36, 18, 18, 18, 24, 19, 23, 20, 21, 19, 20, 20, 21, 19, 18, 18, 19, 23, 17, 21, 19, 20, 19, 20, 21, 21, 19, 18, 23, 17, 20, 22, 17, 19, 24, 20, 21, 21, 19, 19, 19, 20, 19, 18, 22, 21, 18, 21, 20, 19, 19, 20, 20, 18, 18, 22, 22, 28, 20, 19, 19, 20, 20, 23, 24, 19, 16, 22, 19, 18, 18, 19, 18, 20, 21, 20, 18, 22, 22, 23, 21, 18, 18, 20, 19, 20, 18, 20, 21, 18, 20, 25, 19, 19, 19, 18, 21, 22, 29, 20, 17, 19, 20, 21, 22, 22, 18, 18, 20, 20, 17, 20, 22, 19, 19, 20, 20, 20, 19, 18, 20, 19, 21, 21, 21, 30, 19, 24, 23, 18, 20, 24, 19, 19, 19, 20, 22, 21, 23, 25, 20, 22, 21, 25, 21, 18, 19, 23, 28, 34, 21, 30, 20, 21, 23, 22, 25, 20, 21, 20, 19, 23, 18, 21, 25, 17, 25, 24, 20, 24, 21, 18, 33, 23, 19, 19, 18, 19, 18, 19, 23, 17, 21, 24, 24, 19, 21, 17, 20, 18, 17, 25, 18, 18, 22, 18, 19, 20, 20, 39, 20, 20, 23, 23, 20, 20, 27, 26, 20, 26, 17, 25, 19, 19, 22, 22, 18, 19, 20, 21, 20, 36, 22, 20, 29, 25, 34, 20, 22, 25, 21, 17, 22, 18, 31, 21, 22, 21, 17, 17, 20, 18, 20, 25, 29, 20, 18, 29, 20, 21, 22, 20, 20, 18, 18, 20, 22, 21, 20, 18, 22, 22, 19, 22, 20, 21, 30, 17, 18, 20, 23, 38, 20, 23, 22, 20, 22, 24, 19, 20, 24, 21, 18, 28, 20, 20, 28, 27, 25, 20, 21, 18, 19, 21, 22, 23, 21, 21, 18, 28, 22, 20, 19, 22, 36, 27, 20, 19, 20, 19, 21, 24, 21, 24, 20, 25, 19, 22, 25, 40, 22, 32, 21, 22, 17, 27, 18, 24, 18, 27, 21, 28, 21, 26, 32, 18, 21, 19, 20, 22, 19, 17, 22, 24, 21, 16, 22, 26, 20, 20, 21, 26, 18, 20, 18, 24, 18, 19, 19, 21, 17, 18, 18, 20, 26, 28, 22, 25, 23, 21, 17, 21, 19, 20, 17, 19, 17, 24, 16, 27, 21, 19, 19, 18, 22, 25, 19, 19, 21, 20, 20, 17, 19, 20, 20, 22, 19, 19, 23, 22, 21, 21, 19, 20, 25, 23, 20, 19, 23, 22, 20, 19, 17, 19, 23, 19, 20, 18, 20, 27, 18, 20, 22, 24, 22, 22, 21, 21, 21, 22, 21, 20, 17, 20, 24, 22, 22, 20, 17, 20, 22, 18, 20, 19, 33, 19, 34, 18, 22, 19, 18, 22, 24, 17, 18, 21, 22, 21, 21, 24, 19, 18, 20, 20, 21, 20, 22, 21, 21, 19, 22, 20, 19, 18, 20, 25, 20, 17, 18, 22, 24, 20, 17, 18, 21, 17, 19, 23, 25, 17, 19, 24, 19, 26, 31, 32, 21, 19, 19, 20, 20, 19, 21, 20, 19, 20, 17, 20, 23, 21, 22, 25, 21, 20, 20, 36, 18, 23, 23, 21, 19, 19, 18, 23, 21, 19, 32, 23, 21, 18, 17, 23, 31, 26, 20, 19, 27, 20, 18, 18, 19, 18, 20, 28, 21, 21, 22, 20, 21, 20, 27, 21, 21, 18, 19, 27, 25, 23, 18, 18, 21, 31, 18, 20, 20, 23, 21, 20, 19, 29, 18, 18, 18, 18, 20, 20, 22, 25, 18, 19, 19, 22, 22, 20, 21, 19, 19, 22, 21, 17, 23, 21, 22, 32, 20, 21, 19, 28, 24, 21, 17, 21, 26, 24, 22, 19, 22, 21, 19, 17, 35, 23, 21, 20, 22, 20, 20, 20, 28, 21, 23, 25, 21, 23, 23, 40, 36, 20, 21, 20, 34, 22, 20, 38, 22, 20, 17, 25, 17, 20, 18, 19, 25, 17, 19, 23, 31, 18, 17, 21, 18, 23, 20, 18, 18, 18, 19, 18, 29, 22, 22, 21, 22, 20, 30, 20, 28, 21, 21, 25, 20, 23, 25, 20, 27, 18, 21, 21, 21, 20, 22, 22, 21, 20, 17, 20, 19, 26, 20, 20, 21, 25, 28, 24, 25, 18, 22, 23, 20, 18, 21, 20, 21, 30, 30, 24, 26, 25, 21, 20, 20, 25, 19, 30, 27, 35, 19, 18, 24, 21, 18, 22, 21, 20, 23, 22, 21, 33, 25, 27, 24, 25, 20, 23, 19, 18, 22, 28, 21, 18, 23, 18, 20, 19, 21, 17, 23, 27, 21, 19, 18, 24, 21, 18, 19, 35, 21, 21, 22, 37, 22, 19, 19, 18, 26, 26, 28, 37, 22, 22, 28, 21, 21, 25, 23, 20, 22, 19, 23, 20, 23, 23, 17, 20, 27, 23, 18, 22, 28, 21, 19, 26, 23, 18, 20, 20, 20, 16, 21, 20, 23, 20, 18, 22, 18, 25, 24, 18, 20, 20, 22, 20, 20, 20, 19, 18, 25, 21, 17, 23, 21, 22, 24, 18, 20, 23, 19, 19, 18, 21, 21, 20, 20, 25, 24, 24, 17, 22, 20, 21, 19, 24, 20, 17, 21, 19, 28, 21, 17, 28, 19, 33, 27, 17, 18, 19, 17, 23, 21, 19, 23, 23, 24, 30, 27, 19, 23, 18, 17, 24, 31, 18, 21, 23, 18, 21, 31, 22, 19, 23, 31, 21, 16, 19, 19, 23, 20, 18, 34, 19, 20, 21, 17, 18, 21, 18, 20, 20, 19, 22, 21, 18, 24, 22, 22, 23, 19, 24, 20, 23, 28, 27, 28, 22, 22, 22, 24, 29, 21, 25, 33, 18, 23, 19, 26, 22, 22, 27, 21, 22, 16, 20, 32, 37, 22, 17, 20, 18, 29, 22, 20, 20, 35, 28, 22, 19, 24, 17, 33, 22, 20, 21, 21, 17, 21, 24, 25, 19, 19, 18, 19, 19, 35, 20, 31, 21, 19, 23, 21, 28, 26, 22, 20, 22, 31, 23, 20, 25, 21, 18, 37, 28, 22, 19, 22, 24, 26, 19, 19, 31, 22, 19, 21, 27, 20, 22, 22, 27, 17, 24, 24, 21, 20, 22, 22, 21, 25, 21, 19, 24, 21, 19, 25, 26, 22, 32, 21, 23, 21, 25, 21, 24, 19, 20, 23, 21, 23, 22, 20, 19, 31, 22, 22, 21, 22, 22, 22, 17, 20, 19, 24, 24, 18, 19, 21, 25, 26, 19, 31, 30, 21, 21, 24, 21, 18, 31, 19, 23, 19, 19, 18, 22, 18, 18, 19, 19, 21, 26, 27, 24, 22, 21, 20, 21, 22, 33, 23, 19, 24, 22, 21, 23, 18, 20, 19, 21, 23, 21, 17, 30, 28, 18, 27, 18, 17, 19, 18, 26, 21, 21, 19, 29, 22, 28, 18, 24, 25, 20, 20, 33, 28, 18, 24, 19, 25, 23, 19, 35, 19, 22, 19, 26, 24, 22, 26, 35, 20, 20, 18, 28, 22, 18, 25, 21, 21, 20, 36, 22, 28, 22, 22, 18, 23, 21, 21, 21, 21, 20, 28, 19, 21, 18, 18, 19, 20, 21, 18, 19, 24, 21, 24, 29, 27, 20, 26, 23, 19, 22, 23, 19, 23, 21, 21, 26, 18, 19, 23, 24, 22, 19, 19, 20, 21, 20, 19, 22, 24, 26, 20, 22, 23, 26, 30, 23, 21, 22, 21, 23, 20, 21, 24, 24, 21, 26, 22, 22, 27, 26, 27, 27, 27, 19, 20, 23, 19, 28, 26, 18, 19, 19, 19, 21, 18, 22, 20, 19, 24, 22, 17, 20, 19, 19, 25, 31, 20, 20, 23, 25, 29, 21, 22, 25, 20, 21, 19, 33, 22, 17, 23, 21, 21, 19, 21, 21, 19, 29, 20, 18, 41, 27, 24, 24, 21, 30, 24, 19, 24, 22, 20, 22, 26, 22, 19, 21, 37, 26, 20, 18, 23, 19, 25, 23, 32, 23, 22, 20, 34, 26, 21, 22, 21, 23, 26, 23, 25, 23, 24, 37, 26, 22, 22, 24, 26, 23, 21, 22, 23, 17, 20, 23, 25, 20, 21, 26, 20, 20, 23, 18, 19, 20, 21, 28, 21, 18, 20, 25, 23, 20, 23, 21, 21, 17, 19, 22, 25, 21, 19, 24, 17, 20, 20, 21, 23, 30, 24, 22, 18, 20, 20, 24, 24, 29, 23, 19, 20, 19, 22, 19, 25, 25, 20, 19, 19, 21, 28, 18, 27, 32, 17, 21, 18, 20, 21, 20, 21, 23, 19, 19, 20, 21, 21, 21, 21, 19, 23, 19, 19, 22, 23, 19, 23, 20, 22, 19, 21, 19, 22, 24, 21, 20, 29, 19, 22, 25, 17, 17, 21, 30, 22, 19, 21, 19, 20, 18, 23, 22, 22, 20, 23, 19, 17, 19, 25, 22, 21, 22, 23, 19, 20, 24, 17, 20, 21, 21, 20, 19, 26, 20, 25, 24, 21, 22, 24, 21, 29, 19, 22, 23, 20, 25, 21, 25, 23, 21, 20, 19, 25, 20, 20, 21, 19, 19, 19, 21, 20, 22, 17, 19, 19, 21, 23, 21, 23, 30, 22, 22, 20, 20, 25, 25, 25, 19, 25, 29, 20, 20, 23, 20, 23, 24, 22, 20, 17, 23, 28, 22, 33, 29, 28, 29, 19, 23, 21, 20, 18, 24, 21, 19, 19, 22, 21, 18, 19, 19, 19, 18, 19, 19, 20, 27, 20, 20, 19, 18, 18, 22, 19, 19, 22, 21, 23, 22, 22, 28, 19, 19, 24, 20, 21, 21, 29, 19, 35, 20, 20, 23, 18, 21, 19, 22, 20, 18, 22, 21, 24, 24, 21, 21, 19, 17, 28, 28, 19, 22, 22, 21, 24, 22, 21, 20, 22, 22, 22, 25, 34, 28, 20, 24, 23, 25, 19, 20, 20, 19, 20, 23, 26, 22, 22, 20, 24, 22, 32, 20, 19, 23, 18, 21, 20, 22, 23, 24, 19, 19, 32, 21, 27, 21, 22, 24, 19, 20, 19, 19, 20, 22, 18, 23, 31, 29, 23, 20, 29, 22, 25, 22, 35, 25, 18, 19, 22, 19, 17, 24, 28, 21, 20, 25, 27, 27, 29, 21, 19, 19, 24, 19, 18, 17, 20, 23, 18, 25, 22, 20, 19, 26, 27, 22, 17, 23, 22, 26, 26, 27, 25, 22, 39, 20, 19, 18, 21, 23, 20, 17, 32, 26, 23, 20, 24, 22, 18, 18, 22, 20, 19, 28, 20, 20, 24, 23, 21, 22, 26, 25, 31, 24, 20, 28, 23, 24, 20, 28, 25, 22, 17, 22, 20, 37, 24, 18, 30, 25, 25, 20, 21, 26, 29, 20, 27, 22, 22, 24, 21, 27, 35, 29, 18, 21, 21, 31, 28, 17, 20, 22, 26, 24, 24, 22, 24, 31, 21, 24, 22, 18, 26, 25, 21, 19, 22, 28, 20, 23, 23, 19, 18, 25, 23, 21, 23, 20, 18, 23, 28, 19, 21, 19, 21, 19, 30, 20, 25, 23, 22, 25, 29, 20, 25, 19, 21, 24, 26, 19, 20, 19, 21, 23, 19, 20, 26, 31, 18, 18, 21, 37, 20, 30, 24, 26, 19, 22, 20, 19, 30, 20, 21, 26, 19, 22, 20, 20, 19, 21, 24, 27, 25, 34, 19, 22, 23, 27, 27, 18, 21, 18, 19, 21, 20, 27, 24, 21, 19, 19, 20, 23, 20, 19, 18, 20, 19, 20, 24, 18, 25, 19, 23, 24, 23, 20, 24, 21, 18, 22, 22, 34, 24, 28, 20, 18, 24, 21, 25, 23, 19, 20, 21, 19, 25, 19, 36, 24, 25, 18, 29, 28, 17, 21, 23, 26, 21, 18, 21, 30, 24, 19, 20, 23, 29, 23, 19, 24, 20, 20, 20, 34, 22, 24, 24, 27, 27, 28, 22, 20, 29, 22, 19, 21, 28, 26, 24, 22, 20, 22, 20, 35, 18, 34, 24, 23, 26, 20, 20, 22, 20, 21, 23, 22, 25, 21, 23, 20, 21, 32, 19, 22, 20, 23, 20, 18, 20, 20, 29, 28, 25, 29, 39, 18, 31, 21, 21, 26, 29, 29, 25, 31, 34, 19, 30, 27, 18, 21, 22, 23, 22, 17, 21, 27, 20, 19, 20, 23, 23, 20, 20, 23, 18, 26, 24, 20, 21, 19, 19, 25, 26, 23, 22, 24, 20, 21, 23, 25, 18, 21, 26, 23, 18, 21, 25, 21, 19, 24, 24, 22, 20, 24, 30, 25, 22, 29, 29, 21, 21, 22, 19, 18, 20, 17, 22, 21, 20, 23, 18, 20, 19, 26, 23, 19, 23, 19, 18, 32, 20, 27, 19, 26, 18, 21, 21, 19, 22, 32, 25, 27, 19, 23, 29, 27, 22, 24, 21, 21, 25, 22, 22, 23, 26, 22, 20, 25, 20, 19, 27, 22, 23, 20, 22, 21, 28, 24, 19, 20, 25, 17, 23, 18, 23, 22, 26, 18, 17, 21, 18, 21, 20, 26, 19, 26, 17, 19, 20, 19, 19, 26, 22, 22, 26, 27, 19, 23, 32, 20, 22, 28, 19, 27, 20, 18, 20, 31, 19, 24, 21, 20, 24, 28, 19, 21, 23, 17, 20, 19, 21, 22, 24, 21, 22, 30, 21, 18, 26, 19, 24, 19, 23, 22, 22, 25, 19, 17, 24, 28, 22, 21, 20, 22, 26, 19, 21, 20, 18, 22, 24, 21, 22, 22, 21, 18, 20, 33, 25, 18, 22, 20, 24, 25, 19, 26, 31, 20, 34, 21, 22, 25, 24, 21, 21, 19, 30, 22, 21, 27, 26, 28, 25, 21, 20, 19, 18, 18, 23, 22, 18, 20, 27, 21, 30, 19, 19, 24, 23, 29, 20, 20, 20, 24, 21, 20, 20, 19, 20, 32, 27, 29, 20, 27, 24, 22, 19, 22, 22, 22, 28, 21, 22, 18, 22, 24, 32, 23, 24, 23, 20, 19, 19, 24, 22, 32, 34, 25, 24, 28, 20, 18, 21, 26, 20, 22, 17, 18, 21, 37, 18, 33, 20, 23, 20, 22, 22, 22, 18, 28, 21, 27, 21, 27, 26, 27, 24, 22, 19, 21, 19, 21, 18, 18, 17, 22, 26, 17, 22, 31, 24, 17, 20, 18, 33, 24, 31, 20, 25, 22, 20, 34, 23, 19, 24, 21, 21, 22, 19, 24, 25, 22, 24, 31, 23, 33, 18, 33, 20, 20, 18, 27, 24, 20, 20, 24, 19, 22, 23, 21, 22, 21, 25, 21, 19, 21, 21, 37, 21, 24, 24, 26, 20, 19, 21, 23, 30, 19, 22, 28, 27, 20, 20, 23, 23, 28, 20, 25, 20, 20, 21, 19, 21, 20, 23, 18, 19, 22, 21, 32, 20, 24, 20, 18, 20, 20, 21, 21, 18, 24, 22, 22, 27, 27, 29, 18, 29, 19, 21, 20, 31, 22, 19, 21, 26, 23, 19, 27, 19, 20, 22, 23, 19, 22, 23, 21, 20, 24, 23, 28, 19, 27, 24, 19, 28, 29, 20, 25, 25, 24, 21, 24, 22, 23, 22, 32, 22, 25, 21, 22, 24, 19, 19, 20, 29, 26, 18, 23, 19, 21, 34, 20, 25, 23, 24, 18, 22, 28, 19, 19, 20, 34, 23, 27, 23, 29, 31, 19, 22, 28, 28, 19, 21, 22, 21, 21, 19, 23, 25, 20, 25, 40, 20, 24, 23, 23, 29, 25, 29, 23, 25, 27, 32, 34, 20, 22, 28, 33, 32, 28, 27, 27, 19, 22, 28, 30, 23, 31, 27, 29, 26, 27, 31, 21, 20, 26, 19, 24, 22, 21, 18, 22, 19, 26, 32, 21, 22, 28, 32, 28, 18, 21, 24, 19, 23, 18, 25, 23, 32, 29, 23, 22, 20, 21, 20, 20, 22, 23, 30, 29, 18, 20, 19, 18, 26, 25, 20, 27, 24, 19, 22, 29, 33, 21, 21, 22, 25, 22, 19, 26, 21, 23, 20, 19, 27, 27, 24, 28, 24, 29, 27, 29, 26, 20, 20, 19, 22, 26, 23, 26, 21, 20, 20, 27, 28, 23, 18, 21, 17, 25, 21, 23, 17, 27, 20, 23, 24, 29, 25, 24, 28, 21, 24, 25, 20, 25, 21, 27, 22, 22, 22, 19, 20, 25, 22, 20, 19, 25, 36, 26, 23, 33, 27, 18, 32, 26, 31, 21, 20, 25, 27, 20, 26, 20, 17, 37, 35, 28, 31, 32, 27, 24, 20, 25, 22, 22, 23, 36, 25, 28, 20, 26, 23, 20, 24, 23, 21, 31, 26, 21, 21, 18, 35, 26, 26, 25, 28, 21, 35, 25, 27, 25, 24, 21, 20, 23, 28, 21, 20, 19, 27, 34, 22, 27, 22, 23, 30, 22, 23, 29, 20, 20, 19, 25, 21, 20, 17, 28, 32, 25, 19, 24, 26, 21, 23, 20, 26, 28, 27, 21, 27, 22, 18, 16, 18, 22, 32, 22, 19, 20, 23, 19, 26, 20, 20, 20, 26, 29, 21, 20, 20, 21, 28, 29, 26, 20, 20, 22, 25, 22, 21, 32, 18, 24, 26, 17, 23, 22, 22, 18, 22, 19, 22, 22, 19, 23, 25, 28, 19, 22, 17, 16, 17, 23, 18, 27, 23, 21, 19, 22, 23, 31, 24, 27, 28, 32, 21, 29, 24, 22, 19, 22, 22, 23, 21, 25, 20, 19, 30, 25, 20, 17, 21, 27, 31, 22, 24, 22, 21, 24, 20, 19, 24, 20, 31, 25, 22, 20, 18, 23, 20, 20, 29, 32, 31, 21, 30, 18, 20, 31, 35, 24, 26, 20, 19, 20, 23, 20, 32, 19, 26, 24, 24, 19, 33, 25, 24, 29, 19, 25, 23, 24, 20, 23, 19, 32, 21, 32, 27, 23, 23, 23, 23, 21, 22, 27, 18, 20, 25, 21, 24, 25, 21, 22, 25, 20, 22, 20, 23, 20, 21, 23, 24, 23, 19, 27, 19, 22, 26, 21, 25, 21, 22, 20, 21, 18, 20, 23, 26, 23, 29, 26, 24, 20, 22, 30, 20, 27, 18, 35, 21, 25, 20, 19, 24, 26, 25, 25, 26, 20, 23, 25, 30, 27, 21, 21, 20, 20, 26, 23, 24, 27, 30, 33, 23, 18, 21, 21, 26, 19, 18, 23, 21, 27, 20, 18, 32, 21, 26, 20, 22, 21, 20, 22, 24, 19, 25, 23, 19, 33, 21, 21, 23, 23, 26, 25, 18, 22, 19, 32, 22, 21, 23, 19, 19, 24, 19, 21, 23, 22, 34, 29, 26, 23, 18, 22, 24, 23, 33, 31, 20, 27, 34, 28, 22, 26, 28, 21, 38, 23, 18, 27, 26, 21, 22, 24, 32, 25, 23, 25, 24, 19, 27, 29, 20, 21, 23, 22, 19, 28, 31, 21, 24, 19, 23, 21, 20, 21, 25, 21, 23, 21, 29, 21, 20, 36, 27, 29, 27, 25, 30, 24, 29, 23, 31, 19, 24, 18, 28, 33, 23, 18, 24, 32, 21, 25, 23, 21, 27, 20, 23, 24, 22, 21, 30, 24, 20, 23, 23, 17, 17, 26, 30, 21, 20, 22, 26, 25, 23, 20, 23, 21, 19, 22, 20, 18, 22, 18, 22, 27, 25, 24, 32, 26, 24, 31, 21, 21, 22, 18, 23, 19, 28, 26, 20, 28, 30, 19, 19, 31, 26, 25, 22, 22, 28, 26, 27, 28, 23, 21, 22, 20, 29, 17, 22, 18, 28, 32, 31, 24, 22, 22, 21, 21, 31, 18, 23, 32, 24, 26, 27, 26, 21, 21, 21, 30, 18, 28, 24, 33, 23, 22, 22, 26, 22, 29, 23, 27, 28, 21, 18, 22, 25, 18, 19, 33, 24, 25, 21, 22, 23, 21, 21, 21, 25, 31, 20, 21, 18, 23, 32, 32, 28, 30, 18, 23, 22, 26, 27, 18, 28, 32, 25, 19, 23, 25, 21, 22, 25, 28, 24, 22, 22, 25, 21, 23, 22, 20, 27, 24, 26, 18, 30, 26, 20, 23, 18, 30, 22, 23, 24, 32, 29, 25, 26, 20, 25, 31, 20, 19, 24, 20, 23, 22, 23, 20, 24, 21, 21, 25, 30, 26, 18, 20, 22, 21, 23, 17, 29, 21, 22, 30, 24, 35, 19, 22, 32, 20, 35, 25, 25, 19, 25, 21, 25, 18, 23, 20, 19, 19, 20, 20, 19, 27, 19, 22, 22, 34, 19, 28, 31, 20, 23, 31, 25, 23, 28, 20, 27, 29, 20, 22, 32, 30, 24, 20, 21, 33, 24, 23, 20, 29, 28, 28, 22, 28, 24, 24, 21, 21, 19, 33, 24, 20, 22, 20, 17, 21, 28, 25, 28, 26, 27, 23, 20, 25, 23, 23, 30, 26, 20, 29, 24, 26, 26, 31, 22, 23, 29, 28, 18, 23, 22, 23, 20, 24, 19, 27, 25, 30, 23, 27, 34, 19, 25, 20, 31, 26, 20, 22, 22, 24, 21, 30, 30, 19, 19, 18, 24, 30, 32, 25, 22, 18, 23, 27, 21, 24, 25, 36, 21, 27, 28, 20, 25, 28, 20, 30, 21, 33, 26, 23, 23, 31, 30, 18, 21, 26, 18, 35, 22, 32, 29, 31, 23, 23, 22, 24, 22, 26, 32, 24, 19, 21, 25, 25, 22, 30, 26, 19, 27, 25, 18, 28, 27, 32, 24, 20, 20, 25, 25, 27, 34, 26, 27, 24, 22, 25, 27, 32, 22, 23, 20, 31, 22, 21, 36, 26, 24, 21, 22, 20, 29, 23, 26, 18, 24, 26, 32, 29, 21, 30, 26, 33, 28, 27, 23, 22, 26, 20, 34, 20, 31, 23, 27, 22, 31, 27, 30, 20, 20, 24, 20, 30, 27, 36, 35, 24, 31, 21, 29, 23, 23, 27, 22, 24, 20, 36, 28, 26, 26, 26, 20, 25, 23, 29, 26, 32, 24, 21, 33, 19, 23, 32, 23, 22, 19, 25, 23, 28, 26, 27, 28, 35, 19, 17, 23, 22, 24, 25, 25, 25, 27, 25, 30, 31, 34, 17, 20, 19, 22, 22, 20, 21, 21, 20, 24, 25, 22, 26, 23, 22, 25, 26, 24, 26, 29, 29, 27, 29, 27, 26, 33, 37, 26, 24, 21, 21, 24, 25, 23, 17, 25, 18, 21, 20, 21, 29, 26, 29, 24, 25, 22, 26, 21, 26, 22, 19, 24, 22, 19, 23, 26, 20, 25, 24, 17, 28, 20, 24, 27, 20, 29, 20, 24, 21, 30, 25, 32, 21, 20, 22, 21, 20, 25, 20, 29, 20, 21, 24, 18, 27, 19, 20, 20, 24, 20, 34, 30, 18, 19, 22, 20, 22, 24, 28, 20, 29, 22, 22, 21, 18, 25, 19, 21, 20, 22, 18, 30, 21, 18, 30, 27, 23, 22, 19, 18, 21, 18, 26, 19, 21, 24, 30, 21, 20, 21, 28, 24, 25, 24, 21, 29, 24, 31, 30, 20, 19, 25, 32, 21, 26, 24, 32, 22, 27, 18, 19, 20, 21, 35, 31, 33, 29, 26, 21, 26, 25, 19, 21, 24, 24, 23, 21, 35, 24, 27, 18, 24, 21, 21, 24, 23, 28, 19, 22, 22, 22, 22, 28, 22, 21, 17, 26, 26, 19, 20, 32, 21, 20, 21, 22, 28, 21, 26, 19, 34, 20, 19, 19, 27, 24, 22, 24, 22, 30, 36, 19, 21, 23, 26, 27, 26, 23, 21, 31, 23, 21, 22, 20, 21, 20, 19, 21, 22, 23, 27, 20, 21, 29, 23, 23, 27, 21, 22, 33, 21, 23, 24, 21, 23, 17, 21, 25, 22, 21, 36, 21, 19, 19, 30, 34, 20, 26, 21, 23, 27, 41, 19, 26, 21, 22, 29, 19, 24, 25, 28, 21, 19, 28, 18, 29, 22, 25, 20, 23, 27, 19, 21, 20, 25, 22, 26, 16, 19, 18, 28, 18, 30, 34, 24, 30, 22, 22, 20, 25, 25, 23, 17, 25, 18, 19, 22, 26, 32, 30, 29, 37, 24, 26, 22, 22, 23, 20, 23, 21, 29, 24, 23, 21, 20, 26, 17, 24, 28, 23, 19, 30, 26, 25, 23, 21, 22, 21, 24, 19, 23, 19, 20, 20, 18, 21, 23, 23, 23, 31, 23, 23, 26, 25, 20, 28, 28, 27, 22, 29, 20, 27, 22, 23, 22, 32, 26, 25, 23, 23, 21, 21, 32, 19, 21, 31, 24, 30, 31, 21, 20, 29, 22, 22, 29, 27, 21, 25, 26, 21, 31, 38, 22, 22, 26, 19, 17, 28, 26, 19, 26, 22, 21, 21, 33, 25, 32, 27, 25, 25, 27, 25, 29, 25, 28, 20, 22, 24, 34, 27, 26, 20, 23, 22, 29, 18, 21, 27, 22, 27, 25, 28, 24, 26, 27, 22, 19, 30, 24, 23, 24, 24, 33, 35, 22, 19, 19, 23, 34, 22, 24, 30, 32, 23, 31, 24, 23, 25, 26, 28, 20, 32, 20, 26, 23, 20, 34, 25, 25, 25, 29, 26, 29, 19, 23, 20, 26, 20, 20, 26, 20, 21, 28, 31, 24, 19, 27, 28, 28, 24, 33, 37, 25, 23, 24, 26, 20, 33, 22, 17, 27, 33, 30, 22, 27, 35, 28, 34, 21, 23, 24, 22, 20, 22, 29, 20, 21, 20, 20, 25, 16, 21, 23, 28, 20, 25, 23, 38, 28, 18, 28, 32, 28, 22, 22, 24, 19, 23, 24, 27, 25, 23, 28, 23, 21, 21, 34, 22, 19, 23, 22, 28, 21, 34, 20, 21, 23, 26, 24, 33, 27, 20, 36, 30, 21, 23, 20, 21, 22, 19, 24, 23, 19, 23, 24, 24, 35, 31, 27, 24, 24, 19, 20, 24, 26, 23, 24, 26, 27, 31, 27, 20, 25, 28, 22, 26, 40, 26, 22, 19, 22, 27, 21, 26, 24, 27, 22, 25, 22, 23, 32, 26, 34, 26, 20, 29, 30, 26, 18, 24, 21, 21, 22, 20, 27, 24, 19, 28, 21, 27, 23, 24, 27, 22, 33, 28, 20, 25, 26, 21, 22, 29, 22, 27, 22, 34, 20, 32, 34, 21, 19, 25, 27, 28, 19, 24, 37, 24, 35, 20, 24, 19, 31, 20, 23, 24, 27, 24, 26, 23, 29, 23, 28, 29, 22, 23, 21, 30, 24, 29, 21, 24, 31, 31, 30, 28, 20, 25, 23, 33, 35, 19, 36, 34, 28, 26, 30, 23, 20, 31, 22, 26, 24, 31, 21, 19, 26, 30, 30, 28, 18, 20, 19, 29, 26, 27, 23, 26, 26, 20, 20, 25, 30, 21, 22, 26, 24, 29, 24, 21, 28, 22, 30, 26, 21, 27, 27, 36, 27, 31, 20, 30, 24, 23, 31, 32, 24, 25, 29, 26, 25, 22, 24, 20, 25, 28, 23, 32, 31, 29, 26, 25, 30, 19, 22, 19, 33, 28, 29, 27, 20, 25, 23, 31, 23, 20, 21, 19, 25, 26, 28, 19, 22, 20, 27, 27, 20, 22, 24, 24, 28, 24, 32, 29, 22, 28, 21, 28, 19, 27, 18, 21, 31, 21, 26, 25, 21, 18, 34, 19, 20, 20, 29, 21, 24, 25, 21, 27, 35, 28, 25, 24, 21, 23, 24, 21, 23, 26, 26, 35, 27, 20, 20, 26, 24, 26, 22, 23, 37, 25, 21, 23, 23, 22, 24, 24, 24, 28, 20, 18, 20, 22, 29, 30, 27, 21, 27, 33, 25, 28, 29, 25, 27, 21, 25, 23, 27, 29, 25, 25, 23, 23, 29, 19, 31, 26, 31, 26, 21, 26, 27, 31, 21, 22, 23, 23, 29, 24, 27, 27, 20, 29, 22, 30, 21, 21, 21, 30, 26, 24, 21, 26, 28, 29, 27, 23, 28, 31, 29, 38, 25, 21, 30, 32, 21, 20, 23, 22, 22, 29, 31, 25, 25, 26, 26, 25, 22, 22, 32, 20, 36, 21, 30, 25, 34, 29, 32, 23, 28, 27, 21, 24, 30, 28, 24, 33, 28, 26, 25, 22, 23, 36, 26, 20, 32, 20, 22, 22, 29, 17, 22, 27, 24, 29, 27, 23, 22, 24, 33, 20, 24, 30, 32, 27, 23, 25, 36, 35, 26, 21, 24, 26, 34, 20, 32, 25, 35, 25, 25, 18, 36, 26, 23, 21, 22, 35, 27, 23, 28, 35, 28, 29, 24, 26, 20, 35, 27, 23, 36, 35, 26, 26, 21, 25, 28, 28, 28, 29, 22, 20, 28, 21, 25, 29, 24, 30, 27, 24, 24, 34, 18, 19, 23, 21, 31, 28, 25, 26, 30, 34, 18, 21, 27, 24, 25, 21, 24, 26, 23, 22, 17, 22, 19, 28, 21, 18, 26, 22, 26, 32, 35, 24, 24, 25, 22, 23, 18, 18, 27, 19, 19, 19, 21, 19, 23, 21, 20, 26, 19, 33, 19, 21, 20, 26, 21, 23, 20, 36, 17, 29, 19, 22, 29, 20, 20, 25, 26, 27, 18, 26, 25, 21, 20, 27, 23, 24, 19, 18, 24, 20, 25, 22, 19, 25, 27, 31, 22, 23, 22, 19, 23, 22, 24, 33, 21, 18, 22, 24, 27, 28, 27, 22, 21, 22, 27, 19, 22, 22, 22, 25, 27, 20, 22, 21, 18, 27, 26, 24, 21, 24, 21, 27, 30, 22, 17, 19, 25, 26, 25, 23, 20, 20, 21, 21, 33, 28, 20, 25, 18, 25, 30, 21, 20, 23, 32, 24, 22, 22, 28, 26, 30, 30, 22, 33, 21, 18, 21, 29, 22, 31, 31, 30, 29, 19, 23, 19, 27, 25, 28, 18, 19, 22, 24, 26, 19, 24, 31, 26, 21, 28, 18, 18, 26, 22, 16, 21, 27, 27, 21, 19, 27, 24, 26, 19, 24, 24, 22, 25, 27, 22, 20, 23, 21, 29, 21, 30, 25, 21, 22, 30, 22, 20, 26, 27, 26, 19, 24, 30, 19, 30, 25, 24, 30, 30, 25, 22, 22, 34, 25, 27, 32, 29, 22, 19, 24, 22, 23, 26, 30, 23, 28, 24, 19, 30, 23, 34, 22, 29, 21, 21, 18, 27, 20, 22, 22, 18, 19, 17, 25, 23, 32, 22, 23, 21, 25, 18, 32, 33, 22, 30, 23, 22, 23, 25, 20, 25, 22, 18, 19, 23, 23, 24, 24, 31, 21, 29, 24, 19, 31, 24, 30, 24, 22, 19, 30, 23, 27, 21, 22, 26, 27, 25, 20, 22, 26, 22, 27, 26, 34, 19, 31, 30, 22, 23, 30, 22, 27, 26, 29, 23, 28, 22, 27, 27, 19, 27, 29, 27, 28, 21, 25, 19, 26, 34, 21, 20, 28, 23, 27, 24, 25, 30, 24, 20, 21, 23, 22, 21, 30, 22, 25, 22, 19, 27, 29, 16, 21, 20, 33, 30, 19, 21, 24, 20, 22, 27, 27, 20, 33, 19, 28, 18, 20, 31, 22, 19, 22, 25, 31, 19, 29, 23, 24, 20, 23, 25, 23, 26, 27, 21, 30, 30, 18, 24, 22, 27, 20, 24, 20, 23, 34, 21, 32, 33, 22, 22, 28, 32, 21, 32, 25, 34, 23, 20, 33, 30, 20, 23, 31, 25, 27, 23, 22, 20, 24, 23, 25, 24, 23, 21, 18, 23, 20, 30, 23, 22, 18, 28, 33, 19, 19, 29, 31, 24, 22, 27, 32, 34, 27, 23, 23, 20, 25, 24, 20, 24, 25, 25, 26, 24, 27, 23, 21, 32, 25, 21, 23, 32, 20, 24, 30, 21, 26, 29, 30, 23, 21, 17, 24, 24, 22, 23, 19, 34, 20, 22, 33, 21, 26, 25, 22, 22, 33, 24, 24, 26, 28, 34, 23, 23, 29, 30, 21, 30, 26, 32, 28, 19, 27, 23, 24, 22, 22, 29, 19, 26, 26, 23, 25, 23, 22, 29, 27, 33, 21, 18, 25, 32, 22, 20, 27, 31, 29, 30, 35, 21, 21, 24, 25, 22, 20, 18, 21, 26, 24, 23, 24, 24, 22, 29, 30, 33, 28, 21, 19, 20, 23, 34, 32, 33, 31, 29, 34, 20, 28, 30, 29, 27, 21, 27, 22, 24, 20, 20, 28, 19, 21, 24, 31, 26, 23, 23, 27, 23, 29, 20, 25, 24, 22, 30, 22, 28, 27, 24, 23, 21, 27, 34, 28, 24, 31, 33, 20, 21, 23, 25, 21, 27, 23, 23, 20, 19, 20, 28, 20, 31, 29, 27, 29, 22, 20, 29, 24, 23, 37, 22, 29, 26, 29, 26, 26, 22, 22, 31, 23, 22, 21, 19, 28, 23, 22, 31, 22, 26, 19, 21, 28, 23, 18, 19, 28, 18, 26, 26, 18, 29, 25, 30, 25, 33, 27, 23, 26, 29, 32, 26, 25, 22, 23, 22, 25, 28, 22, 24, 26, 30, 21, 31, 30, 27, 21, 22, 27, 20, 29, 26, 24, 33, 21, 25, 22, 23, 19, 30, 23, 24, 18, 33, 28, 29, 28, 29, 21, 26, 26, 20, 22, 27, 26, 23, 34, 23, 26, 28, 36, 32, 24, 25, 21, 26, 30, 31, 23, 24, 30, 24, 21, 26, 21, 24, 31, 26, 33, 26, 31, 20, 20, 27, 20, 21, 22, 25, 31, 23, 25, 26, 26, 28, 20, 22, 30, 22, 26, 20, 27, 28, 30, 18, 31, 33, 27, 21, 19, 24, 36, 23, 33, 21, 31, 25, 30, 24, 32, 26, 25, 20, 22, 19, 20, 26, 28, 23, 26, 26, 23, 25, 17, 20, 21, 21, 27, 26, 23, 25, 23, 32, 27, 21, 22, 27, 28, 27, 22, 22, 28, 26, 20, 25, 25, 25, 23, 26, 26, 28, 26, 24, 24, 25, 29, 26, 35, 22, 34, 24, 29, 25, 20, 25, 26, 31, 21, 26, 21, 24, 24, 25, 35, 22, 25, 24, 27, 26, 21, 28, 27, 20, 24, 19, 24, 31, 28, 21, 33, 27, 27, 26, 30, 30, 28, 30, 34, 22, 24, 24, 34, 19, 36, 37, 19, 26, 27, 18, 37, 36, 29, 20, 27, 20, 32, 30, 20, 19, 24, 31, 18, 34, 23, 28, 22, 26, 27, 29, 22, 21, 30, 26, 17, 23, 29, 25, 31, 25, 32, 23, 30, 26, 26, 26, 26, 24, 21, 21, 23, 29, 23, 24, 29, 35, 36, 32, 22, 26, 23, 28, 22, 35, 23, 26, 26, 21, 34, 22, 20, 23, 21, 30, 23, 21, 26, 24, 30, 25, 23, 20, 32, 22, 24, 22, 23, 27, 29, 20, 27, 21, 30, 31, 34, 29, 26, 29, 27, 23, 28, 27, 26, 22, 23, 31, 26, 24, 22, 26, 25, 26, 26, 23, 25, 20, 31, 25, 28, 23, 21, 29, 22, 31, 29, 20, 33, 28, 31, 23, 25, 25, 28, 24, 30, 22, 21, 23, 28, 18, 21, 24, 23, 28, 34, 28, 24, 33, 21, 24, 30, 27, 28, 23, 25, 28, 24, 26, 32, 32, 21, 22, 22, 28, 26, 24, 28, 24, 28, 21, 31, 21, 21, 22, 34, 34, 29, 18, 24, 24, 36, 24, 26, 26, 36, 20, 28, 33, 27, 23, 29, 29, 23, 28, 26, 32, 35, 26, 27, 35, 31, 27, 20, 31, 39, 30, 29, 23, 24, 37, 25, 29, 27, 36, 31, 21, 26, 26, 30, 24, 22, 24, 36, 32, 24, 21, 26, 26, 31, 18, 20, 33, 26, 20, 26, 26, 32, 30, 33, 26, 23, 21, 20, 20, 21, 28, 23, 27, 25, 26, 23, 31, 19, 21, 34, 26, 20, 29, 27, 20, 34, 22, 22, 19, 31, 23, 24, 23, 24, 22, 21, 17, 26, 19, 25, 21, 19, 33, 23, 25, 19, 28, 25, 22, 35, 27, 23, 28, 26, 21, 30, 24, 23, 25, 27, 27, 26, 19, 22, 24, 20, 27, 20, 27, 25, 20, 22, 19, 26, 19, 30, 25, 22, 22, 27, 23, 22, 24, 22, 28, 25, 22, 22, 21, 21, 36, 32, 31, 24, 33, 32, 26, 28, 26, 27, 23, 22, 21, 21, 21, 21, 20, 22, 22, 20, 26, 28, 23, 25, 22, 27, 30, 24, 30, 22, 21, 28, 29, 26, 27, 23, 22, 29, 20, 22, 29, 21, 21, 25, 25, 25, 23, 32, 21, 21, 24, 24, 19, 27, 25, 20, 19, 30, 21, 21, 28, 31, 22, 23, 28, 26, 34, 26, 20, 27, 34, 21, 25, 21, 19, 30, 22, 19, 26, 26, 20, 24, 27, 28, 17, 23, 21, 28, 28, 27, 22, 21, 19, 24, 26, 25, 22, 26, 25, 23, 25, 31, 18, 18, 22, 32, 22, 21, 20, 23, 31, 31, 21, 25, 29, 25, 32, 23, 29, 20, 28, 21, 22, 33, 20, 24, 23, 19, 35, 25, 27, 22, 23, 26, 24, 29, 25, 23, 18, 32, 22, 20, 31, 28, 26, 28, 28, 22, 23, 23, 23, 31, 26, 27, 25, 26, 27, 20, 27, 23, 18, 38, 29, 20, 26, 32, 18, 20, 17, 22, 31, 23, 27, 28, 25, 23, 22, 27, 24, 26, 19, 20, 22, 25, 26, 28, 21, 21, 24, 24, 30, 25, 25, 24, 26, 25, 30, 26, 26, 26, 23, 22, 26, 25, 33, 25, 24, 24, 24, 18, 21, 19, 21, 20, 21, 28, 30, 20, 25, 25, 33, 26, 22, 23, 25, 28, 23, 21, 24, 27, 24, 23, 19, 32, 39, 23, 32, 22, 24, 27, 19, 25, 20, 24, 26, 26, 20, 17, 25, 21, 24, 25, 21, 19, 29, 18, 22, 27, 26, 32, 25, 31, 22, 20, 24, 27, 26, 24, 25, 27, 22, 23, 20, 33, 23, 26, 31, 24, 22, 28, 24, 24, 24, 26, 21, 28, 26, 31, 27, 34, 22, 24, 19, 24, 21, 25, 29, 24, 26, 32, 21, 24, 20, 21, 31, 32, 21, 24, 23, 38, 32, 24, 36, 22, 22, 20, 28, 32, 30, 22, 26, 29, 28, 23, 20, 28, 21, 21, 19, 22, 28, 26, 27, 27, 29, 28, 19, 24, 21, 30, 24, 30, 25, 28, 28, 22, 24, 29, 26, 27, 26, 24, 35, 32, 22, 24, 23, 21, 22, 23, 25, 35, 21, 19, 27, 22, 26, 28, 19, 24, 26, 25, 30, 24, 21, 25, 31, 25, 26, 35, 24, 22, 32, 32, 23, 25, 22, 28, 26, 35, 21, 26, 27, 30, 30, 26, 22, 23, 29, 26, 23, 23, 24, 18, 22, 20, 27, 29, 28, 25, 29, 24, 26, 22, 29, 31, 26, 22, 33, 18, 22, 25, 21, 30, 26, 35, 22, 28, 20, 20, 18, 18, 18, 24, 30, 25, 28, 27, 26, 21, 21, 22, 23, 28, 27, 27, 33, 31, 27, 25, 25, 30, 17, 22, 22, 22, 34, 26, 20, 22, 23, 19, 31, 25, 31, 30, 27, 20, 25, 20, 20, 26, 25, 22, 33, 28, 29, 26, 22, 25, 27, 28, 24, 25, 21, 23, 28, 28, 23, 28, 31, 31, 20, 21, 29, 28, 19, 32, 20, 22, 18, 24, 26, 23, 29, 25, 24, 29, 30, 21, 30, 24, 26, 29, 25, 20, 21, 24, 24, 22, 31, 32, 25, 24, 18, 23, 26, 30, 23, 27, 23, 28, 23, 22, 31, 24, 32, 30, 26, 23, 31, 25, 30, 29, 26, 24, 37, 28, 28, 25, 34, 33, 28, 39, 20, 23, 23, 26, 29, 22, 25, 22, 24, 28, 29, 30, 22, 21, 21, 26, 34, 22, 25, 20, 19, 23, 26, 30, 26, 27, 30, 21, 32, 30, 25, 35, 33, 25, 34, 29, 24, 30, 30, 27, 25, 23, 28, 27, 37, 22, 29, 22, 29, 20, 21, 25, 27, 25, 20, 27, 25, 20, 25, 20, 26, 17, 24, 23, 19, 25, 28, 21, 20, 22, 27, 25, 22, 20, 23, 20, 23, 21, 30, 26, 22, 24, 28, 22, 25, 27, 24, 38, 24, 25, 24, 30, 29, 21, 21, 25, 33, 24, 21, 20, 26, 23, 26, 28, 25, 33, 35, 21, 26, 24, 30, 29, 28, 29, 25, 28, 25, 35, 23, 33, 32, 22, 26, 24, 23, 26, 24, 29, 30, 23, 29, 23, 24, 26, 27, 31, 27, 25, 23, 23, 21, 27, 29, 19, 22, 32, 27, 26, 20, 24, 29, 23, 21, 27, 22, 26, 31, 23, 21, 26, 24, 21, 21, 19, 42, 31, 24, 22, 31, 27, 27, 28, 29, 24, 25, 20, 24, 24, 23, 23, 29, 33, 28, 23, 29, 30, 23, 22, 24, 26, 24, 26, 27, 20, 24, 23, 25, 32, 28, 29, 23, 25, 29, 23, 31, 33, 21, 33, 22, 26, 32, 24, 19, 24, 20, 24, 30, 34, 29, 24, 25, 24, 31, 25, 33, 28, 32, 24, 33, 29, 25, 26, 25, 24, 22, 26, 19, 33, 25, 32, 30, 27, 34, 24, 22, 26, 24, 27, 28, 30, 35, 26, 33, 26, 25, 22, 31, 36, 32, 27, 25, 21, 26, 23, 25, 28, 21, 28, 25, 22, 19, 22, 28, 25, 23, 27, 21, 27, 29, 29, 26, 27, 22, 22, 30, 26, 26, 21, 30, 25, 25, 22, 22, 30, 30, 25, 25, 24, 24, 25, 26, 32, 34, 26, 27, 34, 25, 30, 19, 26, 22, 36, 30, 24, 27, 35, 29, 24, 28, 25, 24, 28, 20, 28, 27, 31, 25, 33, 32, 30, 25, 32, 30, 28, 27, 33, 22, 29, 22, 28, 28, 20, 34, 31, 25, 26, 20, 31, 32, 31, 27, 29, 22, 23, 26, 31, 26, 35, 22, 21, 31, 34, 29, 36, 29, 22, 23, 27, 29, 38, 27, 27, 33, 29, 30, 29, 28, 25, 27, 36, 36, 23, 28, 26, 25, 35, 33, 23, 33, 22, 27, 29, 25, 40, 26, 18, 19, 19, 25, 18, 24, 21, 19, 21, 29, 18, 32, 25, 23, 27, 27, 27, 22, 19, 24, 21, 30, 27, 20, 20, 28, 26, 19, 24, 22, 20, 20, 19, 31, 23, 34, 22, 24, 20, 21, 21, 27, 21, 19, 28, 24, 29, 25, 21, 21, 32, 28, 26, 30, 22, 25, 20, 27, 26, 27, 30, 22, 22, 19, 26, 26, 19, 22, 21, 25, 28, 26, 17, 23, 21, 28, 21, 33, 24, 27, 19, 30, 22, 23, 22, 29, 30, 21, 31, 18, 28, 23, 24, 22, 30, 21, 24, 22, 37, 24, 23, 27, 28, 26, 30, 22, 34, 25, 20, 25, 26, 23, 26, 31, 26, 26, 19, 20, 26, 22, 21, 21, 25, 20, 21, 33, 28, 18, 24, 33, 25, 19, 34, 20, 38, 27, 29, 21, 26, 29, 29, 25, 33, 29, 26, 20, 22, 19, 38, 22, 20, 23, 27, 25, 28, 25, 33, 31, 26, 29, 34, 21, 29, 27, 19, 23, 30, 29, 25, 34, 35, 24, 29, 28, 26, 30, 22, 28, 25, 31, 28, 29, 23, 22, 22, 30, 22, 25, 23, 24, 31, 27, 32, 25, 33, 22, 21, 21, 22, 21, 26, 21, 31, 24, 27, 23, 20, 21, 34, 32, 20, 25, 27, 22, 18, 23, 24, 22, 25, 26, 24, 25, 33, 22, 23, 23, 19, 24, 25, 24, 24, 20, 25, 28, 22, 23, 21, 20, 20, 23, 21, 17, 28, 22, 25, 25, 26, 23, 20, 21, 26, 25, 35, 24, 35, 29, 22, 26, 25, 35, 25, 21, 20, 28, 24, 21, 25, 26, 26, 20, 29, 28, 21, 25, 24, 26, 29, 21, 26, 27, 23, 30, 23, 22, 25, 37, 25, 34, 20, 26, 34, 32, 29, 26, 23, 25, 24, 23, 25, 21, 24, 28, 19, 20, 25, 24, 20, 22, 26, 23, 19, 31, 27, 21, 27, 21, 32, 22, 36, 25, 29, 26, 21, 28, 31, 24, 29, 30, 24, 23, 32, 34, 26, 32, 30, 30, 27, 24, 23, 22, 23, 24, 23, 19, 21, 32, 23, 23, 19, 18, 21, 19, 27, 29, 30, 30, 20, 28, 21, 35, 30, 20, 28, 27, 25, 21, 23, 34, 24, 22, 21, 23, 20, 32, 23, 32, 32, 28, 35, 32, 25, 28, 20, 21, 25, 30, 30, 24, 26, 35, 28, 29, 28, 25, 26, 29, 24, 27, 20, 36, 36, 33, 36, 20, 25, 34, 18, 31, 27, 30, 35, 21, 21, 22, 21, 21, 27, 25, 24, 22, 22, 26, 25, 30, 28, 22, 28, 30, 26, 22, 27, 33, 22, 18, 26, 22, 29, 20, 26, 24, 31, 27, 24, 22, 27, 21, 25, 20, 22, 25, 23, 28, 27, 31, 22, 27, 30, 28, 33, 24, 23, 27, 21, 24, 30, 23, 25, 29, 21, 25, 33, 31, 32, 28, 22, 24, 33, 23, 27, 23, 26, 30, 29, 24, 18, 32, 27, 32, 27, 19, 32, 17, 28, 22, 21, 24, 25, 20, 34, 27, 22, 29, 24, 24, 26, 22, 29, 29, 24, 32, 30, 35, 36, 29, 24, 25, 21, 28, 34, 24, 20, 25, 25, 29, 21, 27, 26, 31, 38, 28, 20, 21, 28, 33, 21, 26, 24, 23, 21, 21, 34, 18, 35, 28, 29, 30, 25, 31, 27, 21, 30, 29, 23, 20, 32, 34, 18, 30, 28, 21, 32, 22, 27, 23, 28, 27, 25, 20, 30, 25, 24, 26, 24, 22, 26, 26, 21, 19, 23, 20, 27, 30, 31, 21, 19, 22, 22, 20, 25, 29, 27, 26, 20, 24, 23, 22, 31, 27, 20, 20, 22, 29, 31, 32, 32, 30, 23, 25, 24, 22, 26, 30, 28, 34, 23, 24, 22, 24, 25, 28, 28, 31, 31, 25, 33, 30, 21, 24, 26, 28, 28, 24, 33, 18, 27, 21, 20, 25, 29, 32, 22, 28, 22, 22, 29, 25, 30, 32, 19, 30, 22, 18, 30, 29, 28, 27, 28, 20, 27, 21, 22, 29, 26, 27, 21, 22, 25, 26, 24, 19, 28, 18, 27, 22, 24, 19, 26, 27, 29, 23, 22, 27, 20, 27, 27, 24, 26, 23, 26, 21, 31, 28, 32, 23, 31, 24, 28, 36, 20, 21, 27, 25, 26, 18, 29, 22, 21, 21, 23, 25, 19, 26, 22, 27, 22, 24, 26, 23, 23, 21, 26, 23, 25, 30, 31, 33, 23, 21, 21, 32, 24, 26, 27, 31, 29, 22, 21, 29, 20, 21, 28, 24, 26, 23, 32, 23, 33, 27, 22, 23, 29, 27, 29, 22, 29, 24, 27, 25, 25, 25, 29, 32, 33, 22, 21, 32, 29, 32, 23, 27, 24, 21, 29, 26, 25, 29, 33, 20, 29, 24, 30, 27, 26, 25, 31, 27, 28, 21, 30, 20, 26, 27, 29, 29, 29, 30, 25, 21, 25, 21, 25, 31, 27, 22, 30, 22, 23, 36, 32, 32, 26, 22, 30, 26, 27, 32, 24, 25, 24, 27, 23, 29, 33, 32, 33, 20, 24, 32, 33, 23, 21, 21, 33, 26, 25, 26, 22, 27, 26, 25, 24, 24, 23, 21, 30, 32, 22, 26, 22, 18, 21, 22, 22, 30, 24, 28, 35, 22, 27, 22, 32, 31, 30, 24, 30, 21, 27, 31, 32, 26, 31, 33, 31, 29, 32, 29, 34, 23, 35, 35, 28, 34, 24, 20, 30, 21, 26, 29, 24, 29, 25, 21, 27, 20, 24, 24, 32, 22, 35, 29, 29, 32, 22, 24, 25, 25, 24, 25, 25, 25, 30, 25, 23, 23, 25, 22, 20, 27, 23, 22, 29, 27, 25, 29, 33, 26, 25, 21, 25, 24, 25, 26, 24, 26, 29, 18, 21, 21, 27, 32, 35, 26, 26, 38, 31, 25, 24, 26, 25, 28, 24, 21, 24, 31, 23, 21, 26, 19, 24, 28, 31, 26, 25, 31, 37, 35, 25, 21, 21, 29, 27, 28, 24, 30, 34, 33, 27, 21, 22, 22, 21, 23, 24, 21, 25, 28, 25, 27, 25, 23, 33, 24, 23, 26, 23, 21, 33, 26, 34, 29, 34, 26, 23, 27, 19, 20, 31, 23, 31, 24, 28, 23, 34, 32, 30, 26, 31, 33, 29, 23, 27, 29, 24, 23, 29, 28, 22, 28, 30, 23, 29, 19, 25, 33, 30, 34, 30, 26, 31, 27, 28, 25, 25, 31, 33, 19, 23, 30, 23, 29, 23, 26, 25, 35, 21, 22, 31, 25, 30, 30, 38, 38, 30, 30, 27, 22, 26, 28, 36, 25, 24, 25, 26, 24, 28, 24, 29, 29, 22, 25, 26, 30, 26, 27, 23, 30, 29, 26, 30, 40, 33, 28, 25, 32, 32, 27, 30, 29, 21, 31, 28, 21, 23, 26, 27, 23, 23, 26, 30, 32, 20, 26, 22, 29, 26, 27, 28, 24, 25, 26, 20, 22, 24, 26, 25, 27, 34, 34, 32, 27, 28, 26, 25, 24, 28, 25, 20, 24, 18, 30, 37, 33, 27, 20, 30, 30, 33, 28, 30, 26, 24, 29, 28, 32, 22, 31, 37, 27, 26, 20, 22, 33, 36, 24, 19, 25, 32, 31, 21, 32, 21, 32, 25, 23, 25, 29, 17, 21, 23, 23, 19, 23, 21, 22, 19, 35, 31, 22, 28, 20, 23, 23, 22, 23, 22, 30, 28, 24, 22, 22, 27, 26, 23, 21, 26, 24, 21, 30, 18, 28, 23, 27, 19, 23, 23, 28, 22, 22, 28, 21, 22, 25, 21, 30, 19, 25, 25, 37, 19, 18, 19, 24, 24, 20, 29, 28, 20, 20, 26, 25, 23, 20, 24, 22, 35, 22, 25, 20, 24, 23, 25, 21, 29, 25, 24, 28, 31, 25, 33, 21, 31, 31, 27, 26, 29, 24, 24, 32, 24, 22, 26, 27, 25, 29, 29, 22, 23, 26, 29, 24, 21, 31, 25, 21, 21, 25, 30, 24, 28, 36, 21, 28, 21, 19, 24, 21, 27, 25, 30, 21, 31, 21, 29, 29, 23, 24, 32, 28, 20, 26, 21, 28, 27, 31, 20, 21, 34, 26, 24, 30, 24, 23, 28, 24, 23, 28, 22, 23, 26, 23, 34, 22, 28, 22, 25, 28, 30, 30, 27, 25, 21, 28, 29, 28, 30, 22, 26, 21, 25, 24, 28, 24, 19, 21, 31, 25, 26, 21, 20, 25, 21, 24, 34, 22, 22, 18, 19, 25, 28, 21, 21, 22, 22, 20, 24, 20, 25, 31, 32, 25, 33, 29, 28, 35, 30, 24, 26, 26, 21, 28, 20, 23, 31, 33, 29, 24, 29, 26, 26, 27, 29, 25, 23, 20, 31, 22, 25, 29, 33, 25, 30, 25, 25, 24, 25, 35, 33, 29, 27, 27, 21, 24, 21, 24, 23, 25, 32, 24, 21, 26, 23, 26, 32, 22, 29, 21, 22, 20, 35, 25, 21, 30, 37, 19, 22, 22, 29, 23, 30, 29, 22, 29, 31, 27, 31, 26, 22, 30, 24, 27, 27, 31, 29, 24, 36, 30, 27, 24, 30, 21, 23, 30, 24, 27, 20, 23, 32, 20, 26, 29, 27, 21, 27, 23, 26, 25, 26, 30, 31, 31, 26, 25, 28, 25, 27, 28, 23, 31, 26, 32, 23, 28, 22, 32, 23, 31, 20, 22, 21, 31, 24, 20, 22, 25, 28, 27, 32, 29, 22, 26, 28, 35, 27, 21, 23, 34, 23, 28, 26, 26, 34, 24, 19, 30, 22, 25, 26, 35, 22, 26, 25, 25, 24, 23, 31, 26, 33, 30, 31, 21, 21, 34, 24, 29, 25, 28, 26, 22, 21, 25, 27, 33, 20, 26, 24, 32, 21, 30, 24, 28, 27, 25, 27, 26, 22, 22, 18, 33, 35, 28, 21, 18, 25, 25, 23, 23, 24, 22, 23, 26, 29, 30, 27, 20, 18, 19, 29, 24, 22, 27, 28, 22, 25, 29, 28, 23, 23, 26, 25, 26, 25, 23, 28, 28, 27, 27, 28, 34, 29, 30, 24, 29, 26, 24, 28, 22, 21, 31, 22, 29, 25, 25, 25, 29, 26, 27, 26, 21, 24, 23, 21, 30, 19, 24, 28, 26, 29, 26, 22, 32, 24, 33, 20, 25, 21, 25, 26, 28, 24, 33, 34, 31, 25, 25, 22, 28, 27, 22, 34, 24, 26, 28, 31, 26, 27, 26, 22, 30, 31, 30, 24, 24, 31, 24, 26, 31, 23, 26, 25, 24, 25, 28, 37, 25, 19, 25, 23, 25, 28, 28, 28, 29, 30, 29, 30, 24, 26, 25, 22, 27, 23, 22, 22, 34, 28, 20, 26, 32, 23, 21, 23, 27, 29, 31, 20, 25, 24, 20, 33, 34, 29, 25, 18, 31, 28, 32, 22, 22, 23, 20, 24, 24, 26, 19, 25, 24, 30, 26, 32, 27, 28, 26, 31, 19, 25, 24, 21, 25, 26, 29, 24, 22, 33, 36, 32, 23, 36, 20, 24, 25, 21, 29, 28, 31, 26, 26, 27, 26, 31, 31, 31, 29, 31, 29, 25, 32, 22, 24, 25, 30, 22, 20, 27, 36, 21, 28, 28, 26, 24, 28, 24, 25, 30, 31, 24, 24, 25, 26, 24, 26, 20, 26, 30, 30, 28, 23, 27, 29, 23, 30, 21, 30, 23, 24, 30, 26, 31, 24, 24, 33, 25, 28, 24, 30, 25, 23, 27, 31, 23, 20, 20, 23, 19, 28, 25, 24, 24, 22, 28, 22, 34, 25, 24, 21, 28, 21, 34, 34, 30, 26, 26, 30, 30, 29, 30, 22, 26, 24, 22, 24, 22, 20, 29, 23, 21, 30, 20, 30, 26, 25, 23, 34, 23, 29, 26, 31, 24, 26, 22, 24, 27, 28, 29, 34, 24, 22, 26, 32, 29, 26, 29, 24, 23, 30, 32, 34, 31, 19, 26, 28, 22, 21, 30, 19, 23, 23, 22, 30, 29, 26, 36, 22, 25, 32, 34, 29, 29, 21, 28, 27, 24, 22, 23, 25, 30, 23, 22, 24, 26, 28, 28, 36, 25, 27, 30, 21, 29, 26, 22, 28, 27, 29, 28, 27, 22, 28, 23, 34, 28, 32, 27, 32, 22, 25, 22, 22, 31, 32, 30, 30, 34, 21, 21, 18, 23, 26, 23, 25, 34, 30, 29, 27, 24, 28, 31, 33, 25, 30, 21, 19, 26, 26, 29, 22, 29, 29, 29, 34, 23, 35, 26, 34, 32, 24, 24, 35, 24, 21, 17, 22, 26, 20, 29, 27, 21, 28, 24, 20, 30, 32, 33, 28, 27, 22, 22, 29, 25, 29, 29, 25, 23, 23, 31, 28, 27, 26, 32, 27, 29, 36, 33, 26, 22, 22, 34, 21, 23, 31, 21, 21, 23, 21, 36, 23, 18, 20, 29, 30, 29, 21, 26, 22, 28, 24, 28, 21, 21, 23, 26, 24, 21, 23, 23, 26, 24, 28, 22, 29, 26, 29, 35, 29, 27, 31, 24, 25, 28, 27, 25, 25, 21, 27, 23, 27, 21, 37, 33, 33, 26, 29, 25, 29, 29, 25, 24, 24, 29, 32, 34, 30, 36, 27, 24, 36, 22, 26, 24, 27, 24, 34, 26, 28, 22, 29, 36, 34, 27, 23, 28, 24, 25, 35, 33, 21, 29, 25, 26, 28, 24, 26, 21, 33, 21, 24, 25, 32, 24, 24, 26, 28, 30, 22, 30, 25, 33, 30, 35, 24, 34, 23, 25, 27, 24, 32, 25, 35, 24, 26, 34, 22, 29, 27, 30, 26, 26, 26, 24, 27, 30, 30, 29, 29, 22, 23, 33, 35, 27, 27, 25, 27, 29, 28, 29, 23, 24, 30, 25, 28, 32, 28, 27, 32, 24, 24, 26, 26, 38, 26, 31, 25, 20, 24, 20, 23, 24, 35, 32, 25, 33, 25, 26, 26, 30, 31, 31, 21, 26, 25, 36, 24, 23, 28, 25, 24, 30, 28, 26, 30, 33, 27, 34, 33, 24, 22, 24, 21, 24, 27, 23, 29, 36, 25, 31, 29, 34, 26, 19, 26, 22, 24, 29, 28, 20, 30, 23, 28, 19, 33, 22, 25, 26, 36, 24, 28, 23, 24, 24, 26, 29, 24, 31, 21, 26, 23, 23, 29, 26, 32, 24, 20, 24, 23, 21, 34, 22, 21, 26, 30, 29, 20, 24, 21, 30, 24, 20, 27, 30, 22, 27, 23, 29, 21, 24, 25, 27, 23, 22, 26, 24, 34, 23, 23, 27, 26, 26, 29, 25, 26, 27, 36, 22, 33, 26, 26, 30, 29, 19, 19, 23, 25, 21, 31, 22, 26, 27, 19, 28, 23, 35, 27, 20, 22, 25, 22, 34, 23, 26, 26, 19, 25, 23, 22, 29, 30, 27, 20, 29, 26, 29, 25, 30, 25, 29, 31, 36, 20, 32, 26, 19, 21, 26, 22, 26, 21, 20, 26, 30, 30, 25, 28, 28, 22, 24, 21, 24, 25, 21, 23, 29, 24, 23, 33, 23, 27, 24, 33, 22, 31, 17, 31, 24, 27, 24, 22, 29, 22, 27, 20, 21, 23, 33, 30, 26, 30, 25, 34, 21, 28, 29, 29, 27, 26, 34, 23, 23, 30, 28, 31, 34, 24, 25, 28, 24, 21, 27, 32, 22, 26, 26, 18, 26, 34, 23, 27, 21, 30, 27, 32, 25, 27, 30, 30, 25, 26, 19, 20, 27, 25, 28, 27, 23, 26, 26, 26, 27, 30, 25, 28, 28, 31, 29, 23, 18, 24, 21, 22, 23, 29, 22, 22, 32, 28, 22, 25, 31, 24, 19, 21, 24, 23, 25, 25, 22, 25, 30, 24, 25, 28, 23, 22, 24, 23, 30, 27, 21, 30, 25, 27, 26, 34, 32, 29, 25, 24, 30, 29, 25, 33, 20, 28, 26, 25, 25, 29, 31, 28, 21, 32, 24, 26, 23, 29, 30, 33, 26, 23, 24, 25, 22, 19, 21, 22, 25, 30, 21, 20, 24, 33, 27, 32, 25, 30, 28, 21, 23, 22, 23, 20, 23, 33, 25, 25, 26, 29, 20, 23, 26, 23, 30, 34, 26, 34, 27, 27, 22, 34, 35, 25, 23, 26, 24, 24, 26, 25, 27, 27, 29, 23, 29, 26, 21, 33, 25, 20, 21, 24, 28, 20, 18, 27, 26, 24, 24, 23, 21, 23, 24, 28, 28, 29, 26, 22, 29, 24, 20, 28, 24, 33, 26, 24, 24, 28, 21, 23, 20, 26, 22, 30, 33, 26, 24, 29, 28, 32, 41, 29, 22, 28, 24, 28, 22, 20, 31, 23, 24, 28, 28, 32, 26, 30, 33, 24, 26, 21, 25, 24, 24, 31, 28, 23, 28, 22, 23, 33, 27, 29, 27, 31, 28, 29, 25, 21, 23, 26, 21, 22, 24, 27, 21, 25, 30, 21, 28, 30, 34, 28, 23, 31, 28, 20, 23, 25, 24, 27, 24, 24, 32, 29, 24, 28, 22, 28, 26, 29, 34, 35, 33, 23, 23, 31, 27, 26, 23, 20, 18, 22, 25, 21, 30, 36, 24, 34, 20, 21, 27, 24, 25, 34, 34, 34, 25, 31, 21, 22, 31, 22, 19, 24, 24, 26, 28, 25, 26, 28, 30, 21, 20, 23, 34, 24, 27, 21, 32, 34, 30, 30, 25, 23, 35, 23, 24, 37, 21, 23, 20, 23, 21, 30, 28, 31, 17, 23, 31, 29, 23, 30, 26, 31, 35, 27, 26, 24, 29, 29, 26, 19, 29, 21, 20, 20, 29, 26, 30, 24, 29, 26, 24, 28, 24, 24, 34, 26, 27, 25, 29, 32, 26, 25, 21, 28, 26, 25, 32, 23, 30, 24, 29, 27, 34, 29, 22, 23, 23, 23, 31, 27, 30, 31, 28, 20, 26, 28, 24, 26, 29, 23, 29, 20, 26, 29, 29, 27, 30, 31, 33, 29, 26, 24, 28, 25, 28, 18, 28, 33, 23, 29, 24, 21, 32, 25, 33, 22, 26, 24, 27, 19, 20, 24, 26, 22, 29, 30, 19, 29, 32, 23, 27, 22, 24, 25, 34, 33, 25, 29, 25, 32, 21, 31, 23, 23, 30, 31, 25, 26, 25, 29, 24, 22, 26, 29, 30, 34, 26, 25, 30, 25, 24, 25, 27, 25, 25, 26, 34, 28, 29, 30, 26, 27, 22, 21, 21, 21, 25, 21, 23, 24, 29, 29, 36, 24, 31, 30, 28, 31, 28, 26, 28, 30, 30, 34, 19, 23, 25, 26, 19, 27, 24, 27, 30, 28, 32, 27, 21, 25, 23, 21, 30, 26, 21, 23, 30, 36, 22, 24, 22, 35, 31, 28, 25, 28, 24, 24, 22, 34, 25, 24, 34, 25, 20, 27, 26, 23, 26, 32, 34, 33, 34, 23, 27, 23, 28, 28, 26, 30, 20, 33, 34, 31, 27, 29, 31, 30, 29, 30, 26, 26, 26, 23, 23, 22, 21, 29, 28, 25, 25, 27, 25, 25, 21, 23, 26, 28, 20, 32, 33, 31, 39, 29, 22, 37, 26, 27, 24, 30, 23, 32, 27, 38, 30, 29, 28, 27, 23, 23, 24, 26, 21, 31, 26, 27, 30, 30, 26, 21, 29, 32, 32, 32, 28, 34, 32, 25, 27, 21, 31, 29, 27, 24, 26, 25, 30, 26, 25, 28, 34, 23, 28, 33, 29, 21, 18, 26, 23, 23, 28, 25, 39, 32, 18, 24, 25, 32, 32, 25, 29, 21, 34, 27, 28, 27, 28, 27, 24, 36, 32, 22, 27, 32, 27, 25, 24, 24, 29, 29, 31, 22, 26, 25, 31, 30, 26, 33, 29, 28, 24, 27, 24, 25, 33, 28, 20, 25, 25, 20, 23, 29, 25, 21, 29, 25, 27, 39, 33, 31, 31, 23, 23, 28, 26, 25, 24, 26, 25, 25, 31, 26, 25, 20, 24, 28, 24, 22, 34, 29, 29, 32, 27, 21, 25, 28, 24, 27, 28, 30, 29, 26, 31, 29, 22, 28, 35, 24, 27, 31, 25, 34, 32, 24, 31, 25, 27, 27, 31, 27, 26, 22, 32, 25, 24, 30, 24, 34, 21, 28, 28, 26, 30, 28, 29, 25, 29, 27, 30, 27, 34, 30, 31, 33, 27, 27, 25, 30, 26, 24, 28, 32, 30, 34, 32, 26, 25, 26, 30, 30, 29, 29, 30, 24, 17, 26, 29, 32, 32, 26, 29, 35, 28, 25, 23, 22, 31, 27, 28, 35, 33, 31, 24, 29, 20, 27, 25, 27, 24, 20, 30, 28, 27, 34, 31, 33, 20, 30, 34, 27, 23, 23, 29, 35, 31, 25, 32, 23, 28, 24, 29, 22, 29, 19, 29, 33, 31, 29, 27, 27, 31, 30, 31, 27, 29, 27, 28, 26, 29, 30, 25, 33, 18, 23, 20, 27, 25, 28, 27, 30, 30, 20, 28, 27, 31, 34, 29, 23, 20, 20, 30, 33, 21, 29, 26, 27, 28, 27, 25, 23, 20, 21, 20, 24, 21, 24, 26, 26, 22, 23, 22, 20, 21, 27, 21, 24, 29, 26, 25, 26, 27, 30, 24, 21, 20, 28, 21, 20, 24, 25, 29, 28, 22, 24, 33, 24, 28, 30, 25, 21, 26, 28, 22, 22, 29, 22, 31, 35, 23, 29, 25, 28, 29, 24, 21, 30, 27, 31, 24, 18, 26, 26, 31, 31, 28, 19, 28, 22, 20, 30, 29, 22, 29, 30, 25, 24, 25, 25, 20, 24, 23, 23, 24, 30, 26, 26, 26, 21, 28, 23, 33, 23, 18, 27, 28, 28, 35, 25, 24, 23, 31, 24, 30, 29, 24, 28, 21, 29, 26, 29, 25, 23, 27, 19, 20, 30, 27, 26, 21, 27, 36, 26, 32, 29, 27, 33, 24, 22, 22, 25, 28, 22, 31, 26, 27, 36, 22, 23, 19, 25, 21, 26, 33, 24, 28, 24, 29, 24, 21, 30, 21, 19, 21, 26, 30, 31, 35, 25, 24, 25, 26, 27, 33, 21, 32, 26, 36, 21, 23, 21, 28, 26, 23, 18, 21, 25, 22, 25, 24, 22, 23, 19, 31, 32, 20, 34, 30, 26, 25, 22, 25, 27, 30, 30, 25, 24, 32, 27, 29, 20, 25, 22, 32, 38, 23, 32, 30, 26, 31, 25, 29, 25, 23, 27, 25, 30, 20, 30, 22, 28, 27, 20, 30, 26, 26, 27, 37, 27, 28, 26, 27, 24, 27, 31, 24, 26, 30, 19, 22, 27, 30, 27, 24, 27, 23, 29, 20, 23, 24, 23, 27, 26, 31, 22, 30, 27, 29, 23, 30, 23, 23, 21, 28, 27, 35, 24, 27, 20, 33, 24, 20, 24, 26, 22, 24, 24, 32, 24, 28, 21, 26, 27, 22, 24, 31, 23, 29, 32, 25, 25, 28, 32, 32, 27, 26, 22, 22, 30, 28, 22, 23, 26, 23, 28, 33, 35, 33, 25, 30, 27, 19, 19, 36, 26, 29, 24, 24, 23, 31, 25, 27, 33, 24, 27, 32, 26, 22, 26, 35, 20, 21, 32, 23, 26, 24, 30, 27, 20, 30, 23, 27, 27, 30, 33, 31, 31, 26, 24, 27, 24, 25, 27, 23, 31, 32, 20, 29, 19, 20, 22, 26, 32, 30, 33, 28, 20, 25, 25, 28, 28, 21, 18, 31, 25, 30, 24, 34, 24, 32, 24, 23, 22, 26, 29, 34, 28, 26, 28, 22, 34, 27, 25, 27, 24, 29, 34, 23, 31, 30, 27, 27, 27, 31, 24, 26, 25, 29, 23, 33, 26, 26, 25, 25, 27, 28, 35, 20, 20, 22, 21, 33, 20, 23, 26, 32, 32, 23, 24, 23, 30, 26, 28, 19, 26, 22, 20, 27, 30, 20, 23, 25, 27, 27, 22, 21, 21, 23, 22, 34, 26, 24, 26, 24, 29, 35, 23, 26, 27, 29, 24, 24, 33, 25, 24, 28, 29, 28, 23, 27, 22, 25, 27, 26, 23, 28, 30, 28, 22, 36, 28, 34, 21, 28, 23, 24, 22, 30, 27, 29, 21, 30, 23, 27, 24, 30, 30, 28, 30, 30, 30, 37, 34, 31, 25, 25, 31, 29, 33, 23, 31, 20, 28, 22, 32, 20, 29, 27, 29, 23, 32, 33, 23, 28, 34, 20, 20, 19, 20, 23, 24, 25, 34, 23, 29, 24, 23, 26, 32, 26, 29, 25, 26, 21, 28, 26, 30, 26, 25, 26, 27, 27, 26, 23, 26, 25, 29, 35, 25, 32, 19, 20, 28, 24, 29, 21, 21, 21, 23, 31, 34, 29, 31, 18, 30, 23, 23, 31, 29, 31, 34, 23, 25, 27, 27, 33, 24, 28, 25, 24, 35, 21, 31, 27, 24, 22, 28, 26, 21, 23, 30, 32, 25, 29, 29, 27, 31, 32, 21, 29, 27, 25, 24, 23, 27, 27, 23, 29, 29, 23, 28, 21, 32, 23, 26, 32, 28, 25, 24, 34, 26, 28, 27, 24, 24, 27, 28, 22, 33, 24, 30, 21, 29, 26, 21, 32, 30, 29, 38, 33, 26, 23, 21, 24, 30, 22, 29, 23, 30, 28, 31, 26, 26, 34, 33, 33, 32, 36, 27, 26, 30, 29, 24, 35, 25, 27, 30, 32, 29, 25, 26, 24, 21, 22, 27, 25, 27, 25, 27, 23, 25, 22, 30, 27, 26, 25, 32, 24, 32, 30, 34, 28, 27, 25, 28, 19, 18, 25, 27, 34, 30, 25, 25, 20, 28, 24, 27, 27, 22, 28, 21, 25, 36, 20, 23, 29, 23, 27, 27, 35, 26, 27, 36, 27, 30, 24, 29, 24, 28, 25, 23, 31, 23, 26, 32, 29, 24, 28, 21, 23, 23, 21, 24, 24, 34, 24, 29, 30, 29, 28, 22, 25, 30, 25, 31, 28, 30, 21, 26, 25, 26, 24, 25, 27, 28, 30, 24, 33, 29, 20, 29, 28, 29, 31, 20, 23, 21, 30, 27, 25, 28, 25, 21, 28, 28, 26, 29, 21, 25, 26, 32, 26, 33, 30, 23, 26, 25, 29, 22, 26, 26, 26, 27, 24, 29, 27, 32, 32, 36, 37, 27, 28, 30, 25, 24, 24, 35, 39, 26, 31, 26, 25, 26, 20, 32, 27, 26, 27, 28, 25, 28, 34, 22, 30, 22, 23, 29, 26, 29, 33, 20, 26, 32, 33, 23, 23, 28, 28, 31, 23, 26, 28, 29, 32, 32, 22, 31, 33, 31, 27, 31, 33, 30, 32, 29, 35, 27, 34, 22, 27, 31, 30, 37, 25, 26, 31, 29, 28, 26, 19, 24, 20, 34, 27, 29, 31, 32, 34, 30, 25, 28, 24, 29, 37, 25, 24, 27, 24, 28, 23, 29, 28, 22, 32, 24, 24, 27, 32, 30, 34, 27, 29, 25, 24, 26, 25, 31, 20, 30, 32, 31, 29, 35, 31, 34, 30, 27, 24, 27, 31, 30, 32, 27, 23, 21, 25, 23, 25, 18, 25, 21, 27, 26, 24, 20, 22, 22, 26, 26, 30, 24, 24, 24, 17, 23, 30, 25, 26, 24, 19, 24, 21, 28, 24, 33, 20, 26, 23, 23, 23, 20, 27, 26, 23, 33, 23, 30, 24, 27, 25, 24, 25, 26, 18, 28, 26, 27, 20, 30, 24, 35, 23, 31, 33, 27, 28, 27, 22, 24, 22, 29, 27, 22, 25, 22, 31, 20, 23, 23, 22, 22, 21, 30, 24, 32, 18, 25, 23, 27, 31, 26, 20, 27, 20, 27, 22, 26, 28, 25, 21, 25, 28, 27, 35, 31, 29, 19, 25, 20, 32, 27, 30, 28, 24, 28, 38, 28, 21, 26, 28, 28, 22, 27, 36, 26, 21, 32, 23, 22, 27, 21, 22, 26, 25, 23, 31, 22, 28, 21, 32, 28, 32, 28, 23, 26, 26, 27, 26, 23, 24, 26, 23, 32, 21, 24, 22, 26, 25, 20, 22, 25, 22, 31, 24, 23, 28, 30, 26, 21, 26, 21, 25, 24, 20, 31, 26, 23, 24, 28, 26, 25, 39, 33, 24, 22, 31, 29, 25, 26, 34, 31, 27, 35, 37, 20, 21, 25, 23, 23, 30, 25, 29, 27, 23, 25, 21, 22, 27, 24, 24, 24, 22, 21, 21, 24, 29, 27, 20, 25, 33, 29, 26, 26, 26, 26, 24, 31, 30, 33, 28, 30, 28, 26, 29, 24, 23, 22, 30, 33, 18, 26, 31, 32, 25, 27, 29, 27, 32, 29, 26, 23, 23, 30, 19, 26, 32, 22, 28, 28, 35, 24, 26, 31, 29, 27, 26, 20, 30, 30, 28, 22, 21, 34, 25, 18, 26, 23, 23, 26, 24, 19, 25, 24, 23, 24, 25, 25, 21, 37, 30, 27, 23, 23, 33, 28, 23, 31, 26, 26, 22, 20, 23, 28, 20, 29, 26, 22, 28, 26, 30, 24, 20, 30, 29, 36, 29, 32, 25, 23, 26, 30, 29, 28, 29, 25, 24, 29, 30, 26, 29, 30, 25, 22, 27, 25, 29, 21, 25, 28, 29, 25, 23, 33, 21, 27, 31, 31, 31, 23, 26, 24, 21, 26, 20, 26, 28, 24, 25, 29, 26, 39, 29, 32, 32, 34, 21, 34, 24, 23, 20, 33, 31, 29, 34, 25, 30, 27, 26, 24, 28, 26, 24, 28, 27, 32, 29, 19, 22, 22, 26, 28, 29, 18, 24, 30, 24, 22, 27, 30, 21, 26, 31, 29, 20, 30, 23, 21, 34, 17, 31, 25, 31, 28, 29, 21, 24, 30, 25, 30, 30, 21, 35, 24, 23, 31, 28, 29, 29, 32, 31, 30, 28, 19, 20, 22, 26, 29, 27, 27, 25, 23, 26, 30, 31, 28, 26, 26, 29, 26, 21, 29, 21, 25, 28, 21, 20, 28, 26, 21, 22, 24, 26, 20, 30, 25, 30, 25, 25, 25, 36, 31, 25, 22, 28, 26, 29, 26, 37, 24, 29, 29, 28, 33, 29, 26, 26, 27, 30, 27, 30, 30, 28, 28, 30, 23, 25, 26, 18, 18, 23, 23, 31, 24, 30, 28, 27, 26, 30, 28, 34, 34, 27, 32, 34, 35, 26, 28, 28, 23, 30, 21, 26, 20, 34, 31, 21, 31, 25, 27, 23, 29, 30, 27, 32, 32, 33, 35, 28, 24, 22, 26, 27, 29, 29, 31, 28, 34, 26, 27, 23, 25, 20, 32, 30, 24, 25, 36, 29, 28, 31, 21, 28, 31, 26, 28, 30, 29, 24, 29, 37, 24, 34, 26, 30, 31, 34, 29, 28, 30, 26, 24, 28, 28, 24, 26, 32, 23, 34, 32, 27, 34, 30, 27, 35, 19, 26, 25, 31, 29, 28, 33, 30, 32, 26, 27, 28, 23, 30, 23, 24, 25, 26, 34, 22, 27, 30, 32, 24, 24, 22, 30, 35, 26, 31, 24, 27, 23, 30, 25, 27, 28, 26, 24, 36, 31, 29, 27, 30, 24, 26, 24, 29, 31, 32, 23, 22, 35, 26, 31, 21, 22, 18, 34, 32, 33, 27, 36, 29, 30, 34, 28, 24, 29, 32, 25, 22, 28, 27, 32, 32, 24, 25, 20, 23, 27, 23, 30, 32, 20, 24, 24, 30, 29, 29, 26, 29, 26, 30, 27, 25, 27, 29, 29, 32, 30, 24, 31, 30, 25, 30, 23, 25, 22, 34, 29, 33, 27, 32, 21, 27, 26, 33, 36, 26, 29, 29, 32, 27, 29, 26, 28, 29, 26, 30, 24, 27, 29, 34, 27, 26, 20, 29, 30, 25, 26, 22, 21, 27, 28, 21, 23, 37, 31, 30, 31, 35, 25, 26, 32, 24, 21, 26, 27, 22, 24, 29, 35, 27, 26, 32, 28, 31, 32, 25, 32, 26, 29, 23, 29, 26, 34, 30, 29, 25, 26, 23, 25, 27, 21, 22, 25, 31, 27, 25, 28, 26, 34, 25, 32, 22, 30, 38, 30, 22, 27, 31, 22, 38, 26, 30, 36, 28, 24, 30, 32, 27, 37, 26, 28, 25, 29, 27, 29, 27, 28, 26, 31, 33, 28, 31, 22, 28, 25, 39, 35, 30, 23, 21, 30, 22, 27, 28, 30, 22, 22, 28, 36, 33, 24, 20, 28, 24, 30, 28, 33, 31, 26, 23, 28, 26, 38, 26, 31, 26, 27, 25, 25, 33, 24, 26, 32, 29, 19, 20, 30, 26, 22, 21, 27, 26, 35, 33, 25, 23, 22, 24, 26, 32, 27, 22, 21, 27, 24, 35, 25, 28, 27, 31, 28, 35, 23, 25, 29, 32, 22, 23, 21, 23, 22, 22, 31, 26, 28, 34, 29, 30, 24, 24, 33, 19, 30, 30, 25, 31, 23, 25, 30, 23, 25, 20, 27, 36, 31, 21, 30, 30, 20, 37, 28, 30, 36, 26, 21, 24, 21, 30, 27, 21, 26, 21, 21, 23, 19, 28, 22, 30, 26, 25, 37, 27, 27, 20, 21, 21, 29, 31, 24, 31, 22, 23, 26, 25, 28, 26, 27, 29, 28, 26, 21, 27, 20, 27, 28, 26, 25, 30, 28, 33, 24, 22, 24, 19, 26, 34, 32, 19, 24, 22, 19, 21, 25, 27, 22, 34, 27, 32, 24, 31, 22, 32, 25, 31, 24, 25, 26, 19, 34, 30, 36, 27, 30, 27, 40, 21, 24, 32, 29, 31, 29, 36, 24, 29, 22, 23, 30, 35, 22, 25, 26, 34, 30, 28, 21, 23, 31, 27, 28, 27, 21, 24, 30, 22, 26, 26, 26, 24, 23, 31, 21, 28, 21, 23, 24, 30, 31, 37, 23, 32, 22, 27, 23, 20, 25, 22, 26, 32, 28, 22, 31, 22, 20, 26, 22, 24, 25, 22, 32, 24, 34, 34, 20, 26, 26, 31, 30, 28, 23, 28, 25, 30, 26, 34, 29, 25, 28, 27, 36, 28, 24, 23, 31, 24, 26, 29, 29, 32, 31, 22, 33, 22, 27, 25, 30, 31, 25, 38, 23, 22, 27, 29, 21, 20, 23, 25, 21, 27, 24, 32, 30, 34, 28, 39, 32, 25, 22, 27, 23, 26, 30, 29, 29, 24, 27, 24, 27, 21, 23, 30, 34, 27, 25, 28, 30, 34, 23, 27, 31, 29, 32, 29, 27, 26, 30, 31, 30, 35, 24, 26, 33, 29, 31, 27, 26, 30, 30, 30, 26, 30, 25, 23, 26, 24, 31, 25, 26, 24, 20, 25, 30, 28, 24, 25, 27, 23, 25, 24, 31, 24, 19, 22, 26, 31, 30, 32, 34, 28, 24, 30, 21, 22, 27, 32, 35, 35, 25, 25, 26, 27, 20, 23, 19, 20, 22, 38, 27, 26, 22, 28, 28, 25, 41, 32, 29, 23, 26, 26, 27, 30, 24, 24, 37, 26, 31, 34, 28, 25, 45, 27, 24, 27, 33, 32, 34, 27, 24, 28, 21, 25, 30, 22, 33, 29, 29, 35, 28, 34, 22, 21, 29, 31, 27, 24, 26, 26, 21, 28, 28, 27, 30, 34, 26, 25, 29, 33, 27, 28, 29, 27, 30, 25, 27, 27, 25, 24, 19, 22, 23, 28, 23, 37, 27, 37, 27, 23, 23, 32, 28, 26, 25, 23, 34, 32, 23, 35, 22, 28, 33, 17, 25, 29, 32, 29, 26, 20, 30, 30, 25, 33, 28, 26, 27, 31, 30, 26, 29, 23, 32, 26, 35, 26, 28, 29, 24, 29, 36, 24, 35, 21, 26, 22, 26, 23, 22, 22, 30, 22, 20, 23, 25, 26, 31, 28, 27, 31, 21, 33, 35, 31, 28, 30, 31, 25, 23, 22, 29, 29, 27, 29, 31, 23, 20, 23, 29, 27, 22, 23, 28, 32, 22, 31, 36, 23, 29, 26, 28, 25, 34, 22, 32, 21, 20, 28, 23, 34, 33, 29, 28, 29, 25, 31, 23, 26, 23, 27, 26, 34, 32, 25, 23, 32, 22, 28, 22, 29, 33, 19, 28, 34, 34, 31, 27, 24, 26, 21, 20, 30, 29, 27, 29, 32, 32, 33, 29, 33, 28, 34, 32, 27, 22, 31, 22, 30, 26, 26, 29, 28, 22, 29, 29, 29, 37, 34, 38, 28, 23, 21, 24, 23, 21, 24, 25, 23, 29, 31, 25, 18, 21, 25, 28, 23, 26, 32, 30, 24, 28, 36, 30, 32, 28, 23, 29, 24, 30, 37, 35, 19, 31, 28, 34, 30, 24, 30, 33, 25, 27, 36, 34, 27, 25, 31, 21, 29, 29, 24, 34, 23, 20, 21, 31, 27, 27, 23, 34, 26, 30, 32, 25, 25, 22, 34, 25, 30, 31, 27, 28, 24, 33, 26, 26, 24, 25, 24, 31, 39, 27, 25, 27, 30, 31, 34, 33, 21, 23, 29, 28, 28, 29, 27, 27, 34, 29, 27, 30, 26, 24, 29, 32, 33, 25, 38, 33, 24, 32, 28, 24, 19, 27, 26, 23, 25, 25, 33, 32, 30, 27, 22, 21, 24, 26, 22, 24, 33, 28, 26, 27, 26, 31, 22, 30, 20, 34, 33, 35, 23, 26, 24, 34, 26, 30, 23, 23, 39, 30, 26, 21, 27, 23, 28, 27, 22, 30, 24, 24, 29, 25, 23, 24, 28, 30, 25, 31, 32, 30, 25, 33, 26, 24, 23, 28, 32, 29, 26, 29, 23, 21, 30, 27, 30, 33, 33, 30, 30, 27, 28, 27, 32, 30, 31, 34, 27, 31, 25, 33, 33, 31, 34, 34, 31, 26, 32, 21, 32, 30, 25, 30, 35, 26, 31, 28, 22, 27, 22, 32, 26, 23, 25, 22, 26, 30, 20, 23, 30, 34, 25, 23, 26, 26, 32, 28, 26, 24, 25, 32, 23, 33, 32, 25, 24, 22, 20, 24, 26, 32, 30, 31, 22, 21, 23, 25, 21, 26, 22, 32, 22, 21, 31, 21, 27, 24, 24, 26, 27, 23, 21, 28, 28, 28, 26, 26, 32, 31, 22, 25, 19, 29, 26, 27, 23, 26, 26, 32, 19, 30, 23, 30, 32, 26, 34, 24, 28, 21, 21, 28, 19, 18, 28, 22, 25, 32, 33, 27, 27, 23, 25, 33, 20, 23, 20, 23, 25, 24, 28, 30, 19, 23, 26, 25, 34, 26, 26, 30, 27, 27, 24, 34, 26, 26, 27, 26, 34, 31, 26, 29, 27, 24, 20, 19, 30, 28, 25, 33, 30, 33, 26, 23, 18, 26, 27, 30, 25, 25, 29, 24, 25, 21, 27, 24, 21, 24, 23, 24, 27, 28, 32, 35, 31, 21, 31, 26, 20, 24, 30, 31, 31, 23, 28, 31, 31, 19, 23, 23, 27, 23, 27, 28, 24, 21, 23, 26, 21, 29, 25, 23, 25, 26, 23, 40, 30, 34, 33, 24, 23, 28, 20, 30, 25, 28, 23, 20, 31, 21, 30, 34, 19, 23, 26, 22, 31, 23, 29, 19, 28, 26, 22, 23, 31, 29, 30, 28, 30, 22, 31, 25, 25, 23, 27, 25, 17, 26, 24, 26, 24, 25, 24, 27, 28, 36, 31, 26, 24, 36, 28, 31, 25, 36, 20, 22, 21, 27, 25, 26, 28, 31, 30, 28, 18, 20, 21, 30, 31, 27, 25, 32, 27, 31, 29, 21, 24, 24, 27, 27, 30, 34, 20, 23, 28, 22, 21, 28, 24, 23, 31, 28, 32, 31, 31, 23, 27, 26, 31, 20, 25, 24, 28, 23, 28, 28, 23, 30, 24, 34, 27, 28, 30, 33, 26, 23, 31, 29, 31, 29, 22, 25, 18, 30, 27, 29, 28, 27, 25, 29, 27, 25, 30, 22, 25, 32, 26, 32, 27, 30, 35, 23, 26, 24, 28, 28, 26, 28, 29, 24, 20, 24, 32, 25, 26, 34, 28, 34, 23, 26, 27, 30, 26, 33, 35, 34, 26, 29, 24, 21, 27, 29, 31, 24, 25, 34, 32, 25, 26, 29, 23, 37, 20, 24, 26, 26, 28, 23, 35, 31, 25, 27, 38, 34, 31, 39, 24, 23, 22, 31, 30, 25, 31, 23, 31, 27, 22, 26, 34, 32, 22, 26, 24, 32, 18, 26, 34, 28, 31, 24, 28, 25, 24, 21, 25, 24, 28, 34, 22, 33, 29, 20, 28, 24, 34, 22, 28, 24, 21, 22, 25, 28, 27, 30, 19, 21, 32, 24, 30, 31, 30, 26, 30, 28, 30, 27, 30, 28, 24, 28, 21, 27, 27, 25, 22, 32, 26, 26, 34, 27, 30, 27, 32, 27, 37, 35, 34, 26, 21, 26, 23, 22, 21, 32, 32, 29, 38, 27, 26, 24, 26, 25, 29, 37, 32, 21, 22, 21, 26, 28, 28, 31, 33, 28, 22, 26, 30, 33, 33, 33, 33, 27, 25, 26, 18, 31, 31, 28, 28, 23, 27, 23, 29, 23, 26, 34, 27, 34, 29, 25, 24, 22, 28, 26, 24, 33, 27, 32, 27, 31, 29, 28, 24, 21, 22, 26, 37, 24, 21, 29, 23, 25, 26, 25, 32, 31, 36, 29, 33, 30, 21, 23, 27, 25, 25, 28, 34, 26, 22, 25, 24, 24, 28, 29, 30, 29, 25, 22, 22, 21, 30, 29, 34, 31, 30, 31, 26, 24, 22, 26, 26, 19, 25, 36, 37, 30, 31, 27, 28, 35, 27, 32, 32, 25, 24, 27, 25, 34, 31, 30, 29, 26, 27, 34, 26, 29, 26, 29, 28, 28, 36, 26, 34, 28, 26, 35, 24, 23, 29, 28, 26, 34, 23, 32, 31, 30, 29, 27, 28, 31, 23, 24, 30, 25, 27, 33, 32, 24, 25, 33, 25, 28, 26, 25, 25, 29, 25, 28, 25, 27, 25, 30, 32, 26, 25, 33, 26, 33, 28, 31, 26, 31, 22, 26, 25, 24, 25, 27, 25, 33, 26, 33, 21, 33, 29, 28, 25, 25, 21, 30, 31, 24, 28, 25, 26, 24, 35, 34, 29, 38, 27, 30, 27, 30, 33, 23, 29, 31, 34, 26, 23, 24, 25, 24, 25, 21, 32, 26, 32, 35, 26, 32, 39, 23, 32, 28, 25, 29, 30, 20, 25, 31, 26, 23, 31, 21, 25, 29, 38, 29, 25, 33, 25, 27, 34, 22, 31, 22, 38, 30, 29, 27, 28, 36, 32, 22, 30, 24, 21, 31, 22, 28, 18, 27, 32, 32, 28, 28, 32, 20, 24, 35, 23, 29, 25, 24, 27, 24, 25, 28, 23, 34, 34, 32, 27, 28, 24, 28, 20, 29, 28, 30, 38, 21, 26, 27, 26, 26, 23, 23, 26, 19, 29, 29, 26, 19, 29, 21, 28, 28, 30, 25, 20, 25, 37, 24, 30, 24, 23, 30, 32, 23, 22, 23, 24, 23, 28, 23, 30, 31, 20, 21, 27, 25, 34, 31, 25, 28, 25, 25, 26, 25, 29, 25, 26, 33, 27, 34, 25, 24, 26, 32, 20, 28, 21, 19, 25, 27, 33, 31, 31, 28, 26, 26, 24, 21, 29, 31, 24, 23, 20, 27, 22, 31, 25, 26, 24, 28, 26, 32, 33, 32, 31, 22, 30, 30, 26, 25, 23, 21, 25, 24, 23, 24, 32, 26, 31, 28, 33, 26, 28, 36, 28, 29, 23, 34, 22, 26, 30, 29, 33, 21, 20, 25, 26, 30, 25, 22, 23, 26, 26, 27, 30, 27, 18, 34, 26, 28, 27, 27, 23, 28, 25, 22, 26, 24, 27, 24, 23, 30, 20, 21, 23, 30, 33, 31, 26, 29, 27, 26, 26, 31, 33, 31, 32, 23, 30, 29, 21, 23, 28, 26, 29, 25, 20, 34, 27, 34, 34, 26, 21, 21, 30, 23, 21, 26, 26, 20, 25, 26, 25, 23, 22, 23, 27, 25, 25, 34, 30, 23, 29, 23, 26, 34, 31, 28, 37, 29, 24, 29, 28, 28, 29, 35, 27, 24, 30, 27, 21, 26, 30, 32, 26, 21, 24, 23, 22, 18, 27, 34, 29, 31, 23, 22, 34, 28, 23, 25, 30, 29, 28, 23, 28, 29, 25, 27, 32, 28, 32, 27, 29, 27, 23, 20, 23, 22, 26, 28, 31, 35, 30, 28, 31, 24, 31, 24, 25, 21, 28, 24, 29, 28, 27, 25, 30, 27, 28, 32, 22, 22, 28, 30, 29, 22, 28, 22, 22, 34, 23, 29, 26, 28, 23, 29, 30, 25, 24, 28, 22, 23, 21, 25, 21, 26, 24, 29, 31, 31, 29, 24, 26, 30, 20, 29, 32, 33, 28, 23, 25, 31, 29, 37, 33, 30, 30, 20, 29, 22, 30, 33, 30, 28, 33, 35, 32, 30, 22, 28, 34, 37, 28, 29, 34, 31, 28, 33, 39, 39, 26, 25, 26, 28, 27, 32, 26, 28, 33, 21, 21, 35, 19, 26, 34, 27, 30, 25, 23, 27, 26, 31, 29, 23, 27, 29, 32, 28, 29, 30, 31, 25, 30, 34, 21, 28, 28, 27, 30, 32, 19, 31, 32, 32, 32, 26, 22, 25, 30, 23, 25, 30, 27, 31, 26, 28, 31, 21, 27, 23, 25, 23, 22, 20, 31, 27, 27, 29, 35, 31, 32, 25, 25, 25, 40, 27, 26, 31, 28, 34, 29, 25, 30, 26, 30, 25, 24, 37, 27, 33, 25, 28, 29, 28, 26, 26, 27, 24, 34, 20, 31, 31, 24, 22, 22, 24, 30, 27, 32, 26, 26, 29, 36, 27, 27, 24, 34, 31, 21, 23, 29, 32, 31, 30, 20, 26, 28, 29, 23, 25, 27, 25, 26, 27, 23, 26, 26, 28, 29, 32, 26, 28, 22, 29, 31, 30, 31, 31, 28, 32, 24, 24, 30, 24, 25, 29, 29, 20, 31, 30, 29, 29, 31, 31, 37, 25, 31, 27, 24, 28, 33, 36, 32, 27, 32, 27, 26, 37, 33, 28, 31, 24, 32, 33, 31, 27, 30, 28, 25, 25, 25, 26, 26, 27, 21, 26, 27, 26, 31, 28, 35, 34, 29, 22, 29, 26, 32, 27, 31, 38, 30, 29, 24, 30, 26, 32, 30, 26, 29, 35, 28, 27, 34, 27, 27, 20, 33, 29, 33, 27, 28, 25, 22, 26, 24, 27, 27, 24, 25, 33, 25, 20, 27, 28, 30, 28, 21, 27, 21, 19, 20, 20, 32, 27, 21, 25, 23, 26, 27, 27, 31, 22, 27, 26, 23, 24, 25, 24, 31, 27, 21, 21, 34, 34, 28, 25, 32, 24, 23, 34, 34, 33, 28, 22, 29, 21, 19, 24, 27, 25, 25, 29, 31, 35, 27, 26, 32, 23, 27, 21, 20, 27, 24, 31, 31, 26, 32, 28, 29, 25, 23, 21, 30, 30, 24, 27, 33, 29, 27, 23, 24, 30, 34, 23, 22, 25, 25, 24, 28, 31, 23, 33, 29, 22, 22, 25, 26, 28, 28, 34, 27, 27, 24, 29, 24, 36, 31, 24, 27, 32, 33, 25, 28, 26, 23, 23, 21, 26, 24, 26, 27, 28, 21, 26, 29, 21, 26, 34, 23, 32, 32, 24, 29, 29, 29, 22, 24, 26, 20, 27, 26, 22, 28, 22, 26, 24, 25, 30, 26, 30, 23, 28, 30, 31, 24, 26, 31, 27, 22, 24, 24, 29, 35, 23, 27, 24, 23, 26, 19, 21, 30, 31, 34, 33, 22, 26, 28, 24, 34, 30, 34, 23, 30, 26, 20, 27, 27, 23, 21, 20, 23, 28, 34, 29, 30, 35, 30, 30, 27, 29, 31, 26, 26, 24, 26, 35, 30, 33, 32, 30, 28, 25, 29, 34, 22, 26, 28, 23, 21, 28, 26, 19, 28, 20, 32, 22, 24, 27, 31, 26, 33, 23, 32, 25, 24, 30, 27, 24, 29, 26, 27, 26, 28, 32, 37, 29, 29, 25, 37, 23, 22, 29, 30, 28, 24, 26, 29, 22, 33, 30, 27, 24, 27, 27, 27, 25, 32, 33, 27, 32, 33, 33, 25, 23, 20, 21, 30, 24, 33, 21, 24, 31, 31, 35, 26, 25, 32, 25, 24, 28, 31, 20, 32, 28, 30, 30, 32, 27, 27, 24, 26, 31, 28, 30, 34, 28, 22, 27, 30, 19, 26, 22, 32, 30, 27, 28, 20, 29, 25, 28, 30, 33, 21, 24, 22, 26, 23, 28, 29, 21, 36, 27, 30, 26, 29, 31, 28, 23, 27, 28, 23, 34, 25, 32, 29, 31, 30, 27, 25, 24, 30, 22, 33, 34, 28, 24, 28, 25, 26, 28, 32, 31, 31, 25, 22, 27, 25, 26, 32, 26, 30, 25, 25, 24, 26, 27, 23, 26, 21, 25, 30, 33, 27, 32, 20, 25, 28, 27, 24, 22, 25, 24, 34, 30, 34, 30, 26, 33, 36, 30, 25, 29, 29, 30, 20, 26, 26, 26, 26, 37, 30, 29, 33, 27, 32, 31, 28, 24, 23, 29, 27, 34, 30, 32, 32, 31, 30, 28, 32, 30, 22, 34, 20, 34, 28, 30, 29, 30, 30, 23, 27, 35, 35, 26, 29, 39, 19, 29, 24, 24, 27, 28, 29, 30, 27, 28, 27, 27, 24, 26, 28, 25, 29, 33, 29, 26, 30, 25, 31, 32, 25, 28, 28, 25, 32, 28, 29, 26, 25, 29, 23, 24, 23, 38, 32, 35, 22, 28, 28, 26, 26, 24, 26, 34, 31, 34, 30, 27, 25, 29, 21, 28, 23, 28, 30, 28, 22, 31, 36, 25, 34, 26, 20, 26, 27, 34, 26, 24, 26, 33, 30, 24, 19, 25, 28, 22, 31, 23, 20, 28, 27, 28, 26, 25, 25, 25, 26, 26, 19, 24, 22, 25, 27, 22, 23, 27, 26, 28, 23, 30, 24, 28, 26, 27, 25, 31, 31, 30, 25, 27, 19, 21, 33, 31, 28, 30, 25, 27, 27, 27, 28, 24, 27, 20, 28, 29, 22, 27, 30, 28, 31, 25, 29, 34, 23, 26, 22, 31, 24, 20, 24, 39, 32, 21, 31, 26, 31, 25, 29, 20, 24, 25, 23, 29, 25, 27, 23, 24, 25, 28, 30, 23, 24, 29, 23, 26, 18, 31, 34, 23, 25, 23, 22, 25, 27, 28, 23, 24, 24, 24, 28, 20, 26, 31, 25, 26, 26, 32, 20, 25, 28, 26, 24, 27, 24, 22, 22, 28, 22, 30, 23, 28, 35, 29, 32, 32, 22, 24, 26, 20, 28, 25, 25, 29, 25, 21, 31, 27, 26, 26, 27, 32, 29, 27, 28, 26, 30, 29, 29, 31, 31, 27, 21, 27, 22, 20, 31, 26, 26, 25, 19, 30, 28, 23, 28, 31, 19, 22, 23, 33, 27, 21, 26, 29, 34, 23, 30, 25, 24, 25, 33, 26, 21, 21, 26, 25, 36, 30, 33, 30, 24, 24, 26, 26, 26, 31, 33, 26, 37, 27, 27, 25, 32, 30, 23, 24, 30, 23, 28, 30, 26, 21, 24, 34, 29, 29, 30, 28, 20, 27, 26, 23, 23, 26, 29, 33, 23, 22, 29, 24, 26, 28, 26, 27, 25, 31, 30, 27, 23, 33, 32, 21, 24, 22, 27, 25, 31, 28, 34, 23, 30, 33, 29, 23, 33, 27, 25, 33, 24, 24, 27, 22, 26, 23, 23, 32, 31, 25, 26, 30, 28, 21, 23, 30, 26, 24, 37, 19, 29, 33, 27, 34, 32, 25, 32, 28, 21, 25, 28, 20, 29, 32, 27, 23, 22, 30, 21, 26, 22, 34, 28, 24, 29, 21, 33, 34, 29, 31, 23, 29, 31, 29, 20, 21, 33, 28, 30, 30, 36, 34, 26, 25, 37, 23, 28, 32, 29, 29, 25, 27, 26, 34, 25, 26, 31, 30, 24, 21, 29, 23, 22, 34, 32, 29, 23, 28, 33, 33, 26, 32, 29, 33, 26, 28, 36, 25, 23, 32, 29, 31, 25, 28, 30, 25, 21, 19, 25, 29, 26, 26, 30, 27, 37, 25, 27, 25, 21, 26, 23, 27, 33, 28, 22, 27, 33, 26, 35, 26, 34, 33, 28, 29, 29, 34, 22, 25, 28, 23, 25, 28, 22, 27, 24, 31, 22, 30, 27, 21, 29, 28, 24, 28, 24, 23, 37, 26, 37, 30, 33, 24, 29, 28, 26, 35, 26, 35, 30, 25, 31, 32, 24, 29, 30, 24, 33, 25, 22, 25, 31, 25, 23, 23, 27, 31, 28, 21, 34, 29, 27, 27, 23, 33, 31, 23, 31, 24, 30, 26, 24, 27, 36, 30, 24, 29, 29, 26, 34, 29, 30, 29, 26, 32, 22, 37, 35, 23, 33, 24, 25, 35, 28, 19, 31, 28, 24, 29, 25, 34, 28, 29, 32, 30, 29, 34, 31, 22, 21, 21, 24, 25, 27, 28, 25, 22, 31, 31, 22, 21, 30, 30, 27, 24, 23, 33, 25, 32, 30, 20, 30, 22, 23, 27, 27, 31, 26, 22, 28, 26, 29, 24, 26, 25, 34, 24, 28, 27, 34, 27, 33, 32, 22, 26, 30, 30, 28, 28, 22, 22, 26, 25, 31, 28, 29, 24, 28, 30, 32, 24, 29, 32, 28, 20, 25, 22, 22, 24, 33, 31, 26, 28, 28, 22, 30, 33, 19, 24, 28, 31, 30, 29, 30, 25, 25, 27, 28, 29, 25, 25, 27, 26, 30, 24, 31, 27, 20, 33, 31, 23, 26, 29, 24, 22, 23, 27, 25, 22, 26, 24, 29, 27, 26, 30, 22, 26, 23, 23, 29, 30, 23, 26, 28, 31, 27, 26, 32, 23, 31, 33, 28, 35, 22, 27, 22, 33, 25, 30, 28, 21, 27, 23, 21, 21, 35, 28, 23, 31, 24, 25, 26, 34, 30, 30, 27, 33, 29, 22, 26, 24, 24, 27, 33, 21, 21, 27, 26, 28, 33, 28, 22, 25, 29, 27, 31, 31, 33, 28, 28, 25, 27, 22, 34, 31, 24, 23, 25, 26, 30, 31, 23, 27, 20, 34, 26, 26, 26, 22, 24, 22, 24, 30, 25, 24, 28, 27, 24, 23, 26, 21, 26, 26, 27, 24, 27, 24, 29, 30, 34, 23, 28, 26, 27, 25, 29, 29, 25, 28, 33, 29, 29, 29, 29, 26, 20, 25, 29, 21, 25, 31, 31, 28, 26, 29, 31, 33, 35, 30, 26, 33, 31, 23, 28, 28, 25, 32, 29, 24, 22, 27, 30, 31, 19, 29, 24, 34, 28, 26, 28, 29, 36, 31, 32, 32, 32, 36, 30, 28, 24, 32, 30, 22, 30, 27, 33, 20, 31, 27, 32, 30, 26, 27, 31, 23, 24, 26, 24, 23, 30, 28, 24, 20, 28, 24, 27, 29, 30, 32, 25, 22, 28, 30, 24, 30, 27, 27, 29, 30, 28, 28, 31, 23, 30, 28, 21, 31, 27, 27, 26, 31, 28, 27, 24, 28, 25, 31, 26, 29, 28, 30, 25, 26, 25, 30, 30, 26, 25, 29, 21, 29, 33, 40, 22, 30, 28, 28, 26, 30, 20, 30, 33, 30, 31, 20, 27, 25, 30, 28, 27, 30, 24, 33, 26, 24, 28, 26, 32, 22, 26, 25, 26, 35, 28, 25, 30, 28, 29, 20, 23, 30, 27, 30, 26, 24, 29, 24, 21, 37, 21, 30, 21, 21, 22, 23, 24, 28, 27, 33, 27, 24, 29, 36, 24, 30, 33, 29, 25, 34, 21, 25, 27, 30, 26, 24, 29, 21, 24, 26, 34, 27, 32, 34, 31, 27, 28, 30, 34, 29, 34, 35, 33, 27, 21, 36, 23, 27, 32, 28, 25, 31, 32, 34, 28, 17, 21, 27, 24, 30, 22, 30, 27, 27, 29, 24, 29, 23, 25, 30, 22, 31, 21, 22, 20, 30, 34, 28, 25, 20, 23, 30, 27, 25, 23, 23, 25, 33, 25, 23, 29, 25, 21, 26, 24, 25, 30, 28, 23, 28, 21, 31, 26, 28, 30, 18, 27, 30, 29, 25, 28, 31, 27, 34, 21, 29, 23, 26, 32, 26, 24, 31, 22, 28, 28, 30, 22, 28, 32, 26, 25, 24, 27, 29, 32, 34, 28, 20, 23, 30, 27, 32, 21, 31, 27, 21, 27, 30, 35, 27, 29, 37, 27, 27, 26, 23, 25, 29, 28, 29, 28, 28, 24, 29, 32, 33, 21, 23, 24, 34, 32, 31, 31, 30, 28, 25, 27, 29, 21, 32, 23, 25, 33, 31, 28, 27, 24, 25, 32, 25, 20, 31, 32, 29, 30, 28, 28, 23, 23, 24, 33, 33, 28, 23, 25, 23, 19, 27, 34, 24, 35, 27, 23, 29, 32, 34, 30, 28, 31, 30, 26, 28, 23, 28, 25, 41, 29, 26, 29, 30, 32, 27, 27, 23, 28, 25, 34, 23, 28, 32, 25, 24, 30, 24, 30, 23, 29, 28, 35, 35, 29, 28, 27, 24, 22, 28, 24, 30, 34, 34, 34, 31, 28, 29, 25, 26, 28, 21, 28, 21, 32, 32, 37, 27, 28, 23, 23, 23, 27, 22, 30, 30, 31, 30, 25, 23, 24, 25, 25, 19, 29, 23, 30, 30, 25, 22, 30, 25, 21, 20, 23, 29, 21, 20, 28, 24, 24, 29, 22, 22, 28, 26, 34, 26, 25, 26, 21, 32, 23, 23, 21, 19, 22, 29, 21, 26, 25, 26, 25, 27, 26, 24, 23, 32, 32, 29, 30, 30, 31, 25, 21, 25, 33, 30, 28, 29, 28, 22, 27, 31, 31, 25, 25, 32, 23, 25, 27, 21, 24, 27, 26, 29, 33, 24, 25, 22, 26, 21, 23, 28, 24, 23, 27, 30, 40, 31, 25, 24, 29, 27, 23, 24, 30, 24, 21, 20, 26, 27, 29, 34, 26, 26, 35, 23, 31, 29, 22, 31, 34, 27, 23, 27, 31, 24, 26, 27, 19, 26, 33, 25, 27, 28, 32, 25, 24, 26, 27, 27, 25, 28, 29, 28, 24, 26, 25, 30, 25, 29, 20, 26, 26, 26, 27, 23, 30, 26, 29, 24, 27, 30, 29, 23, 32, 30, 24, 24, 30, 23, 32, 26, 21, 21, 27, 21, 25, 27, 26, 26, 22, 31, 21, 29, 20, 32, 19, 22, 29, 24, 23, 23, 24, 25, 25, 29, 21, 24, 23, 28, 29, 25, 26, 24, 23, 26, 31, 28, 26, 37, 27, 28, 31, 35, 26, 26, 22, 29, 29, 30, 30, 23, 27, 27, 31, 22, 29, 25, 25, 28, 28, 34, 28, 34, 23, 29, 33, 28, 24, 28, 29, 28, 21, 30, 25, 34, 27, 28, 27, 27, 32, 27, 32, 20, 28, 27, 22, 34, 25, 26, 27, 26, 24, 26, 25, 20, 24, 28, 30, 22, 22, 28, 23, 26, 28, 27, 25, 29, 28, 30, 30, 29, 26, 27, 23, 29, 28, 30, 26, 25, 28, 28, 25, 27, 29, 32, 27, 32, 26, 28, 21, 25, 34, 31, 28, 21, 22, 25, 28, 31, 33, 31, 29, 28, 25, 31, 32, 33, 30, 31, 28, 32, 24, 25, 24, 30, 27, 28, 30, 24, 30, 26, 30, 31, 32, 23, 25, 32, 25, 30, 24, 26, 25, 33, 23, 25, 22, 29, 22, 30, 22, 30, 26, 28, 31, 26, 31, 22, 20, 24, 34, 33, 30, 32, 28, 27, 30, 24, 26, 31, 24, 30, 32, 27, 23, 34, 34, 24, 23, 28, 28, 27, 33, 26, 21, 27, 34, 32, 22, 24, 31, 28, 24, 31, 24, 21, 28, 21, 33, 28, 25, 29, 22, 26, 25, 28, 22, 28, 27, 28, 36, 21, 25, 28, 26, 24, 32, 27, 31, 33, 34, 34, 23, 21, 32, 29, 27, 24, 31, 28, 26, 31, 26, 28, 26, 33, 25, 28, 24, 26, 25, 32, 28, 27, 19, 24, 34, 28, 28, 31, 21, 24, 26, 29, 33, 39, 23, 26, 29, 34, 31, 27, 27, 28, 27, 31, 31, 27, 32, 32, 29, 36, 24, 26, 32, 24, 22, 25, 25, 25, 25, 31, 25, 33, 30, 30, 24, 22, 24, 31, 25, 23, 29, 22, 25, 25, 33, 21, 29, 21, 31, 30, 29, 22, 24, 32, 24, 28, 20, 22, 24, 25, 26, 24, 28, 25, 26, 33, 31, 29, 32, 36, 24, 32, 26, 29, 27, 25, 25, 27, 29, 24, 31, 27, 32, 24, 30, 24, 27, 23, 20, 25, 35, 33, 24, 28, 30, 29, 27, 26, 29, 28, 28, 22, 28, 25, 32, 28, 25, 33, 27, 28, 29, 34, 25, 31, 23, 22, 26, 30, 31, 25, 31, 25, 32, 28, 24, 22, 25, 28, 30, 30, 25, 30, 31, 27, 23, 21, 27, 35, 27, 30, 36, 26, 30, 25, 27, 24, 23, 27, 21, 27, 27, 26, 31, 21, 24, 25, 28, 26, 33, 32, 29, 30, 22, 27, 25, 24, 23, 31, 37, 29, 23, 29, 26, 27, 28, 29, 28, 25, 27, 31, 23, 26, 34, 26, 28, 29, 31, 22, 29, 32, 29, 22, 37, 23, 32, 25, 27, 25, 30, 27, 31, 26, 32, 18, 31, 32, 26, 19, 32, 36, 31, 27, 26, 25, 22, 30, 23, 25, 26, 28, 21, 27, 26, 28, 27, 25, 24, 25, 24, 22, 28, 35, 26, 24, 21, 27, 26, 29, 26, 22, 22, 28, 31, 26, 27, 24, 24, 31, 24, 30, 29, 23, 27, 28, 26, 22, 24, 30, 23, 23, 29, 33, 30, 28, 33, 34, 26, 26, 30, 28, 33, 23, 31, 29, 29, 27, 27, 30, 29, 25, 35, 31, 22, 29, 25, 26, 30, 34, 30, 23, 30, 25, 28, 25, 30, 30, 32, 31, 26, 34, 28, 24, 22, 31, 25, 24, 29, 24, 26, 22, 27, 34, 23, 22, 27, 29, 32, 26, 26, 30, 24, 32, 28, 29, 29, 37, 31, 31, 22, 28, 27, 23, 29, 27, 29, 26, 29, 32, 31, 31, 24, 26, 22, 23, 30, 23, 33, 29, 23, 30, 30, 35, 27, 32, 32, 29, 31, 29, 28, 25, 35, 36, 25, 23, 33, 34, 23, 26, 27, 27, 29, 28, 22, 28, 28, 26, 29, 27, 29, 25, 31, 24, 26, 31, 31, 29, 25, 24, 30, 30, 31, 25, 28, 31, 31, 27, 25, 27, 26, 26, 19, 26, 26, 26, 30, 29, 33, 28, 31, 26, 30, 29, 33, 40, 30, 27, 27, 24, 29, 31, 26, 33, 24, 32, 26, 32, 28, 32, 29, 25, 32, 27, 27, 27, 32, 31, 26, 31, 33]
>>> clear()
Traceback (most recent call last):



  File "<pyshell#70>", line 1, in <module>
    clear()
NameError: name 'clear' is not defined
>>> 
