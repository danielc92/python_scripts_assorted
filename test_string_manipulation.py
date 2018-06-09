'''
#REMOVE UNWANTED CHARS AND ADDITIONAL SPACES

ok_chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM 1234567890"

text = "the quick  /,./brown .,/ox REALL%,,.Y JUM$PED OVER  jumps ove[][]r  !  the   @%^%6   fence.@%^@$%@"

for letter in text:
    if letter not in ok_chars:
            text = text.replace(letter, "")
            print(letter + " was removed from " + text + ".")

while "  " in text:
    text = text.replace("  ", " ")

print("\n\nCleaned Text: " + text.capitalize())


# BASIC STRING FUNCTIONS
my_string = "bANaNas"

print("original string: " + my_string)
print("capitalize string: " + my_string.capitalize())
print("swapcase string: " + my_string.swapcase())
print("uppercase string: " + my_string.upper())
print("lowercase string: " + my_string.lower())
print("starts with: " + my_string[0])
print("ends with: " + my_string[len(my_string)-1])
print("format string: " + my_string.format())

t_string = my_string.rstrip().lstrip()
print("trim string: " + t_string + " " + str(len(t_string)))

#TUPLES

my_string_tuple = tuple(my_string)
print(my_string_tuple)
print(type(my_string_tuple))


#SPLITTING

email_list = ["brad@dpc.com","anna@outlook.com","brucespruce@yahoo.com","daniel@hotmail.com"]
email_dict = {}
email_list_new = []

for email in email_list:
    email_list_new.append(email.split("@"))

print("\n"+str(email_list_new))
print("\nthere are " +str(len(email_list)) + " items in the list\n")

for n in range(0,len(email_list)):
    email_dict[email_list_new[n][0]] = email_list_new[n][1]

print("Your dictionary: \n" + str(email_dict))

#REVERSING STRINGS/LISTS

mylist = ["this","is","daniels","list"]
mylist_r = []
mylist_r = list(reversed(mylist))

print("\nReverse a list with reversed and list method\n")
print(mylist_r)

mylist = ["this","is","daniels","list"]
mylist_r = []
mylist_length = len(mylist)
counter = mylist_length - 1

while counter > -1:
    mylist_r.append(mylist[counter])
    counter = counter - 1

print("\nReverse a list with in-build methods\n")
print(mylist_r)

mystring = "this is daniels string"
mystring_r = ""
my_string_length = len(mystring)
counter = my_string_length - 1

while counter > -1:
    mystring_r = mystring_r + mystring[counter]
    counter = counter - 1

print("\nReverse a string with in-built methods\n")
print(mystring_r)

#END COMMENT


#COUNTING OCCURENCES IN A LIST

my_list = [1,1,12,3,4,4,"red","red","blue","red","french",4,5,6,6]

print(my_list.count("red"))

tup = (1,2,3,4,5,6,1,2,"empty")
new_list = list(tup)
print(new_list)

#APPEND AND EXTENDING LISTS

my_list = [1,2,3,4,5,1,2,1,3,4,55,12,21]
my_list2 = ["dog","cat","elephant",'gorilla','advaark','dingo']

big_list = [] #extends new lists by adding two lists
big_list.extend(my_list)
big_list.extend(my_list2)
print(big_list)

big_list2 = [] #appends two lists to new list (nested lists)
big_list2.append(my_list)
big_list2.append(my_list2)
print(big_list2)

my_list2.insert(0, "first animal") #inserts item at index 0
my_list2.insert(len(my_list2), "the last animal 1")
my_list2.insert(len(my_list2), "the last animal 2")

print(my_list2)

my_list2.pop(1) #removes item at index 1
print(my_list2)

my_list.sort() #sorting lists
print(my_list)

my_list2.sort() #sorting lists
print(my_list2)

print(sorted(my_list)) #sorted creates new object, whereas sort() does not

#DICTIONARY LOOP
import random

name_list = ["Cristou Kaja","Cogdell Garry","Farndon Robb","Tocknell Brade","Durrell Kelby","Poplee Alwin","Tidman Jacquelin","Ennew Alford","Dunmore Tadio","Gheraldi Kevina","Egerton Kylynn","Kermott Alphonse","Moores Gracie","McCritichie Alonzo","Soane Rosa","Warbey Mark","Messam Darby","Powder Clementia","Kuhnert Diana","Chaff Mycah","Crohan Faunie","Pennings Cyb","O'Currigan Jory","Mincher Dionisio","Mergue Ginelle","Slay Hedda","Checci Hesther","Sunnucks Kerby","Sides Magda","Bleeze Huntley","Saville Sheryl","Yakebovich Marika","Orta Ainslie","Dowzell Shaun","Hebblethwaite Adele","Mingardi Valida","Beuscher Ninnetta","Clewer Elbertina","Kinglesyd Rochelle","Birckmann Viole","Howsin Fidela","Gatesman Pietro","Sanday Flor","Milksop Bryanty","Servant Sammy","Sloan Andie","Lomasna Lexy","Moughton Brod","Gawkes Jammie","Baddam Barny","D'eye Karoline","Codi Rosita","Rasmus Regina","Della Scala Robbin","Schowenburg Wallie","Sidwell Alina","Dodge Noella","Sollam Dee dee","Nicklen Federico","Snare Corilla","Buggs Barri","Wilmott Abra","Frome Danie","Canton Dyanne","Semark Georgeanne","Kippie Halimeda","Lambotin Alard","Redsull Cornie","Scoates Goldina","Lipyeat Demott","Anersen Karlik","Sproson Elfrida","Creber Cornelius","Goodrick Nicko","Shrieve Drucill","Lathee Jessalin","Esmond Dodie","Reames Cristiano","McAless Mahmud","Sinnie Terence","Kalinowsky Nadean","Weatherhogg Siegfried","Chasemoore Octavia","Shave Lishe","Metzke Caren","Dowda Katuscha","Dallan Eleonore","Quartermaine Lutero","Varian Idelle","Allberry Neddie","Charnick Amy","Mabon Mason","Addy Laure","McClinton Allsun","Woolfoot Danita","Maudett Charlot","Alberti Derick","Jodrellec Julienne","Georgeon Kerianne","Reeday Albert","O'Ferris Eliot","Glowacha Fidelio","Mattecot Dorie","Newis Jessee","Rannigan Etan","Pellitt Lianne","Sherston Merrie","Kennford Julie","Alberti Suzanna","Clitsome Amalle","Yitzhak Raddie","Fosserd Gabriela","Jerams Rafaelita","Lamort Mollie","Randell Humberto","Kendrew Kent","Guiduzzi Pryce","Yakebovitch Carey","Massow Elsy","Veltmann Zack","De Vile Tabitha","Aidler Sherm","Guido Derry","Ganning Rik","Doerren Marcelline","Bales Cecil","Duffet Peterus","Wheelwright Clevie","Reglar Gabriele","Willden Arly","Puxley Beverlie","Cramond Dru","Nelsen Rosmunda","Latan Micheline","Pavey Trudey","Pencost Dorotea","Hastin Rosalinde","Carbry Vinson","Jacquemard Ambur","Sturley Jasmina","Ofield Heriberto","Newcomb Retha","Clementson Amara","Elkington Wynnie","Marple Kissee","Broadbere Mikey","Moyles Marylee","Tremaine Thor","Goman Elroy","Ferras Berny","Thynne Alexei","Tante Orlan","Strippling Bren","Lammin Beau","Dunsford Lukas","Barnewille Arvy","Muldownie Marena","Sibbe Emelina","Stevani Pacorro","Styan Berget","Radnedge Garrek","Saby Lem","Deener Kevan","Larciere Bobine","Peris Wilt","Liddington Ariel","Borborough Marion","Oleshunin Dacie","Stive Delmer","Almak Marion","Furniss Kori","Gillet Janenna","Lacelett Dorthy","Swann Wyatt","Ivy Karmen","Rimell Jacki","Pavinese Bondon","Callear Tessa","Fidgett Martie","Spellecy Titus","Dewsbury Roseann","Dahlgren Iona","Bonallick Magdaia","Gorries Farrah","Ivakhno Janis","Strudwick Sterling","Lideard Russell","Farrington Cathi","Tatam Trescha","Papes Sibley","Fellnee Whitman","McKinstry Daisi","Crowcher Sindee","Beglin Maryl","Gages Kristien","Hindmore Tasha","Scaddon Lydon","Rankin Philippine","Langfield Gerardo","Gansbuhler Irene","Paule Hobie","Laterza Noni","McKissack Kerby","Esmonde Jessica","Antonat Flss","Ardy Bonnie","Gummery Filberto","Treswell Terrance","Baselli Modesta","Eliyahu Angelle","Buglar Holly","Vidloc Marti","Choat Lenore","Phoebe Sybille","Boik Ericha","Mahady Norene","Wiseman Lindsay","Manvelle Ker","Joice Ediva","Couves Trstram","Tuke Evita","Lefridge Jud","Pawle Saunders","Bedinham Doralynne","Runcie Francisca","Schutze Willie","Whittaker Ian","Insworth Garwin","Brockett Loretta","Commin Meridith","Covill Leoline","Grainge Kristy","Brosnan Cherri","Pimblott Paddy","Blaver Karyl","Delamar Tania","Biasini Gates","Gaiger Bax","Setterfield Rudolfo","Scarsbrick Robinetta","Tomasello Omar","Blues Halsy","Gagen Taffy","Lowle Cirilo","Danielsson Malchy","Groucutt Tucky","Linskey Boone","De Moreno Davon","Methuen Rita","Luppitt Noell","Woodings Caroljean","Dixon Phil","MacGebenay Garner","Slimon Rupert","Maydwell Sigfried","Bailes Sully","Yair Lise","Rushmer Gates","Rojas Harmonie","Dickon Tori","Inger Julietta","Ponsford Olympe","Knobell Joleen","Van der Daal Dell","Mastrantone Fulton","Joint Marji","McGaugie Alessandro","Kenworthy Concettina","Bough Cazzie","Bollon Meryl","Arnaudin Marie","de Banke Paula","Bardwell Mariya","Staunton Joelynn","Priter Elisa","Brydon Kristien","Jardin Felipe","Craghead Dannie","Pittendreigh Pasquale","Gouge Gualterio","Okeshott Devlin","Tuohy Ginnie","Happert Norby","Trytsman Moreen","McNeachtain Daron","O'Neal Juana","Stredder Ailbert","Bristoe Julie","Swaysland Sindee","Lounds Sharona","Wollaston Bev","Bonellie Joeann","Mongin Dorena","Gilli Alice","Raxworthy Windham","Ciccottini Bendix","Dedon Quincy","Hulbert Bette","Attoe Lindy","Massy Maria","Claasen Zacherie","Provis Valentino","Curm Teressa","Eaken Lila","Twede Cyrille","Jedrzejewski Emlyn","Mapother Bennie","Barnett Selby","Gwilliam Juliana","Tettersell Sauveur","Seden Jordana","Weedall Donny","Hache Lisa","Willeson Gus","Pleasance Thaddus","Sommerfeld Remus","Caroline Goran","Olexa Redd","Stores Cristy","Thickens Natasha","McMurdo Aylmer","McClory Giulietta","Bremner Gaylor","Capinetti Valina","Stango Christiano","Wombwell Ange","Ferriman Cece","Peevor Analiese","Sallery Aggy","Mateev Karoline","Kelberer Misty","Bartosiak Andres","Spearett Amy","Triplow Jobyna","Wellbank Anallise","Oris Dario","Beardsworth Orly","Bruntjen Christian","Spaice Rhody","Abbati Rik","Froggatt Jean","MacLaverty Sissie","Questier Nana","Couth Xever","Jackett Alexandre","Klimowski Jose","Jerwood Pete","Blackbrough Kathryne","Jayes Vic","Lugsdin Althea","Werrilow Cindi","Izakov Delaney","Tacey Pail","Ixer Gar","Bayns Terrance","Ivanilov Linell","Brabender Christabella","Whales Jeffrey","Clousley Imelda","Ikins Shelly","Pallent Latisha","Brogi Dorene","Adlard Rog","Sedgemore Giordano","Stearndale Jermayne","Gurnay Dicky","Salzen Aubree","Becker Bevin","Ungerecht Sigfried","Alam Rex","Maudsley Konstantine","Boland Burgess","Pendrich Ingrim","Coffee Freddi","Gorton Alexio","Soigoux Analiese","Menier Alwyn","Cottem Talya","Langthorne Danni","Rolinson Celeste","Nisuis Verne","Pfeffel Dill","Durand Berri","Raoul Leupold","Helder Wynny","Thickpenny Germaine","Weaving Rasia","Drain Darline","Kopke Gratiana","Marklund Benson","Bundock Selby","Ross Kerby","Dews Ephraim","Ainsby Talya","Colbeck Amerigo","Borer Greg","Sanz Verla","Goeff Sybil","Brunger Hughie","Bernolet Inger","Smalman Jemmy","Dubock Lexi","Ames Ruthann","Mowatt Meredithe","Braidon Padraic","Cocci Devy","Tregona Fenelia","Downer Lara","Faragher Josephine","Clem Othello","Crutcher Matthias","Tarrier Kendre","Menhenitt Sue","Stook Winonah","Pegg Zorah","Walhedd Cathy","Van Niekerk Rafaelia","Crucitti Fleurette","Blenkin Winny","Fairbanks Sammy","Chessil Lesley","McNevin Melesa","Eakley Lela","Tal Ardelis","Tabard Gerladina","Bugby Morse","Copyn Bobine","Krale Finn","Starbuck Olimpia","Clover Anabal","Saphir Gregorius","Aizikov Jessi","Danks Jill","Embury Calhoun","Wildblood Barney","Wisniowski Carlie","Robrose Val","Sallery Caz","Evans Neville","Heaysman Cornell","Mavin Shani","Collinson Isidora","Peacop Fionna","Ellsworthe Blair","Thoms Bevon","Adlard Aubrey","Spivie Athena","Verriour Millicent","Clibbery Skell","Palfreeman Layla","Fashion Rori","Commin Alvinia","Banham Allayne","Muneely Colver","Emmines Julian","Stilly Minta","Rambadt Alfonse","Pankethman Guillemette","Albone Darlleen","Staresmeare Noll","Hitcham Skip","Whitton Tris","Greendale Gino","Branthwaite Ruddie","Dillingham Horatius","Moffatt Rachelle","Jellings Jeffrey","Tourne Korney","Antcliff Paquito","Pinnell Bellina","Corsar Kellyann","Allred Emmery","Decourcy Rosabel","Jovicevic Pru","O'Flynn Matty","Simeone Katey","Ameer-Beg Wynn","Cato Even","Pyecroft Florencia","Feehery Howard","Matts Lynda","Whyatt Madalena","Roly Geoffrey","Goatman Gun","Georgins Valene","Mumbray Giorgia","Steed Crawford","Mapother Janel","Tumielli Gan","Eplett Cherish","Latch Cherice","Harbidge Trevar","Leathlay Daisey","Orviss Koralle","Mishaw Myron","Fourman Allayne","Grishagin Neville","Shepeard Graham","Samuels Theressa","Rushbrooke Ruthie","Antonietti Ase","Brimblecomb Bearnard","Raynes Bernadine","Blakeley Haley","Fattorini Sol","Honywill Haydon","Blunkett Martha","Kirke Koenraad","Jellman Manfred","Desborough Riane","Baake Orran","Reeveley Maryrose","Bursnell Papagena","Lardeux Caren","Markussen Baxter","Mumbeson Eydie","Deschlein Adrienne","Linde Patricio","Killingworth Antone","Vaudre Tresa","Grissett Ira","Piesold Sissy","Penas Wallie","Motte Madelin","Febry Ondrea","Doulden Kerr","Warret Randall","Sylett Jayme","Hosburn Beatrisa","Trengrove Martainn","Pierce Des","Kohen Blondie","Lardier Franky","Leyburn Levi","Seebert Chris","Awde Shamus","Seywood Freeland","Stockney Annamaria","Oby Pembroke","Kullmann Markos","Chinge Ellette","Fennick Bart","Mostyn Ramsay","Geare Merv","Leaning Elisabeth","Probart Errol","Gurney Malinda","McKomb Drusy","Lansdale Idette","Ellings Daveta","Banker Tonye","Heenan Nickolai","Kegan Ogdon","Betteson Normie","Playdon Maxie","Posnett Gardner","McShea Teresita","Hartshorne Orson","Prazer Catharine","Westwell Vern","Kennagh Tamra","Bentsen Halsey","Cressey Halli","Uvedale Bealle","Temprell Duffie","Callacher Kristofor","Whatford Hube","Banbrick Eugenio","De Roeck Alfie","Gilberthorpe Edlin","Jakoubek Emlen","Kinghorne Angelika","Lugsdin Pepita","Sinnott Elenore","Congreave Morgen","Belk Vic","Gaspero Myrilla","Galpin Meade","Rosa Murielle","Kenford Gerrie","Duthy Chuck","Damiral Danell","Ilyushkin Edita","Meachem Katharine","Beers Adore","Hambelton Nadine","Schulze Torin","Beaufoy Zacharie","Ailward Neille","Picken Thea","Pile Ailsun","Alvarado Hussein","Garwood Nikolas","Vlasenko Regine","Hoggan Gus","Souza Andi","Hanlon Freda","Van Castele Donnamarie","Berrick Geraldine","Brindley Salome","Driuzzi Wyatt","Creamen Mufinella","Hutten Annice","Wardlow Vinny","Rosewarne Dana","Hulks Filbert","Draayer Sibeal","McGreal Reade","Berzon Johny","Jermey Jdavie","Braisby Sandye","Meckiff Urbano","Leith-Harvey Lucille","Hubberstey El","Sutterby Winifred","Scarratt Tan","McGorley Garreth","Straughan Rosene","Sleeny Jereme","Yoskowitz Chrisse","Wigsell Neddie","Wiggett Lock","Feilden Noreen","De Minico Odele","Frushard Paxton","Kellington Sara-ann","Guard Brendon","Pullinger Bronny","Sibbit Jesse","Spilisy Corty","Hanshawe Ulberto","Pagitt Filberte","Cripin Blaine","Ettery Magda","Cogle Ferris","Pittford Steffie","Jorgensen Christos","Milborn Sasha","Dowyer Sidnee","Marian Farah","Sorbey Zorana","Palfrie Sim","Di Maria Mylo","Monini Lorette","Fellows Elsie","Souter Ric","Extence Mella","Middlemist Kimberli","Buyers Gino","Livingstone Maritsa","Mattimoe Anthe","Collingdon Annabella","Albisser Man","Gatcliff Margeaux","Meaton Faustine","Andrault Bridie","Pulman Tonya","Matz Kaitlynn","McTear Kirby","Lente Ransell","Artrick Prince","O' Finan Lucy","Ferry Emelia","Baison Dana","Tritten Alverta","Baxstair Holly-anne","Pursglove Melina","O' Connell Pail","Sill Andres","Kettleson Cindelyn","Appleford Selinda","Fieldgate Grover","Fife Coralyn","Reeds Edythe","Dowrey Ossie","Hiner Borden","Escreet Caritta","Kearley Willi","Illing Minnaminnie","Grzelczyk Cathy","Dinse Grace","Le Grove Roxanne","Cornelleau Savina","Wanell Lauren","Huortic Allayne","Coogan Garvin","Cottier Stanley","Steels Brendan","Marcu Isabeau","Quarmby Ali","Anders Drucie","Salzberg Franny","Loadsman Teodorico","Cuerdale Marcille","Hedditeh Cordula","Stanlick Shermie","Kaser Kris","Boggas Lanie","Spollen Elijah","Flounders Birk","Ovendon Derk","Gerrie Janeczka","Whitewood Jill","Horsburgh Jermaine","Petriello Earlie","Melior Dixie","Golston Toni","Shearsby Gun","Lampens Prent","Ewles Kristi","Wason Quinlan","Castiglio Bernardine","Dell Casa Hubie","Burgan Randall","Enrigo Breena","Alvin Ortensia","Hyman Lillian","McEntee Legra","Bottby Tammie","Benneton Elaine","Nairy Moria","Costa Verene","Margerison Marleen","Vearncomb Rochell","Blatherwick Fields","Carse Carley","Briiginshaw Willy","Farrears Roseann","Fingleton Meggy","Adami Jefferson","Thoma Kenna","Durgan Lilli","Hayes Rachael","Allday Dominick","Thuillier Frans","Bisley Kym","Juszczak Kenneth","Bastock Markos","Schruurs Louise","Abbett Cesya","Bartlett Mauricio","Shilliday Morse","Colborn Guinna","Cattonnet Conrado","Swinden Lorant","Ablett Zak","Gehrels Berenice","Petyankin Kinny","Screas Olympie","Preator Brooks","Clemencon Blaine","Ayliff Mora","Rubenchik Locke","Meade Farica","Winscum Ethan","Chater Christean","Bissatt Flin","Dine-Hart Eveleen","Pfeffer Roldan","Base Ralina","Moore Lazare","Harriot Ruddy","Angrave Dev","Mcettrick Kennedy","Choake Marius","Wilfling Corri","Iwanowicz Dion","Dufaire Gianni","Pearch Rachele","Vigneron Keeley","Maciaszczyk Arnaldo","Meadowcroft Cindy","Kienzle Allyn","Sellar Brana","Byrnes Harriet","Axcel Margaretta","Kobel Bee","Meir Onfroi","Rassell Jojo","Bernette Portia","Lambertz Clyve","Coucher Glendon","Halse Tabor","Riccio Venus","Spurman Ruthanne","Toop Ailsun","Molfino Son","Reddy Gerrie","McNeill Rennie","Bernette Esra","Mayworth Phylys","Skivington Maddy","Whardley Ingeborg","Giacomozzo Barde","Mucillo Tressa","Hucke Heall","Pashley Reeva","England Joe","McHaffy Bevin","Caneo Jermaine","Borer Victoir","Verling Gerri","Gerardin Karyl","Ive Carmina","Flinn Doralynn","McKniely Micaela","Tennison Levon","Snowsill Donni","Burgoyne Olivero","Menendez Ora","Attenborrow Masha","Davydenko Monte","Wollard Vanessa","Kingsnorth Gwenore","Ducroe Salim","Schooling Sofia","Hadingham Bevin","Rheam Ethelyn","Sorensen Wrennie","Werrilow Delmor","Vaugham Hannie","Szwarc Adan","Langwade Cornelle","Wankel Hestia","Summerill Thornie","Dignum Alli","Hebborne Fina","Shead Austin","O'Currine Maurine","Maxweell Shawn","Rowson Anne","Keaton Bill","Warboys Tan","Ledingham Anna","Lindeboom Michal","Petche Jermaine","Whodcoat Raoul","Abramof Devlin","Watson-Brown Caro","Iannetti Roanna","Thurman Ramona","Van Oord Denney","MacDonald Mahalia","Cone Della","Bloxsome Roxie","Bendin Vilma","Dewar Tori","Neeson Darelle","Annand Ive","Avrahamy Boniface","Volant Alair","Thorpe Elizabet","Kiehl Barnett","Burfoot Nissa","Shortcliffe Lorrayne","Bollum Pandora","Syrad Adolpho","Mudge Nonna","De Lisle Maryrose","Philpot Cicely","Wimms Esther","Aireton Bil","Bunney Bail","Volant Packston","Ellerker Bernette","Witherbed Shurwood","Whetland Tonie","Darell Garrard","Carlyle Jacquelyn","Sizzey Jeffry","McLenahan Yance","Hechlin Ingeborg","Abramowitch Caresse","Gobat Donni","Masdin Basile","Crehan Morrie","Kirkby Laurianne","Woolfitt Terri","Hewson Julissa","Allridge Hort","Valero Corissa","Haslum Olav","Brogi Edie","Stabbins Jeffy","Flori Clementia","Liles Juline","Gonning Rona","Fitzer Ricki","Galia Andreas","Troke Byrann","Sandeson Susy","Thurske Brana","Simms Patsy","Tooley Niki","Karlsson Babita","Gulley Alric","Holmyard Dianna","Burgum Susanna","Kinver Ric","Stratley Richmond","Abbotts Persis","Salmoni Hagan","Tremathick Deidre","Shakshaft Billie","Merwede Jermayne","Marciskewski Ailee","Gowry Cherice","Grigoli Clementius","Cammis Clem","Brilleman Kerianne","Cunnell Franz","Mummery Mannie","Beavan Leo","Horche Sawyer","Skilbeck Sybil","McKeurton Hobard","Questier Skipton","Peel Torin","Hindrick Malia","Vasilic Barrie","A'field Cly","Crathern Brandice","Bowry Yuma","Greggor Quinta","Carlet Constantina","Forster Shane","Frenzel; Alexandrina","Stolli Dieter","Bramsen Matt","Curwen Wainwright","Maw Farrah","Carberry Patrick","Tottle Bobbie","Russen Gregg","Skipp Piper","Pibworth Erina","Maginot Humfried","de Pinna Hubie","Aspinell Haywood","Rait Paulie","Blew Elvira","Goucher Toby","Braga Malory","Bartlet Evey","Fullick Ware","Sherbrooke Dillie","Doud Twyla","Lindholm Giffy","O'Kinedy Nadya","Borkett Lowe","Zanre Darin","Fields Alf","Luciani Minnie","Gisby Darla","Newlan Orland","Krollman Berkie","Darque Oswald","Tomaini Rosa","Hanwell Fran","Pointon Lorianne","Sheerman Anny","Bauer Earl","Rabb Andreana","Pressnell Shurlock","Bingham Reider","Jeanel Garret","Meade Thea","Critcher Calida","Buckam Christoper","Patrie Rik","Cushion Odie","Tench Gray","Loffel Augy","Queree Perle","Ashington Clyve","Coslett Alicea","Dawdry Aile","Jobling Glennie","Grave Rene","Gebhardt Coraline","Teese Jeanelle","Polhill Hanson","Blackater Cassandra","Foxen Dermot","Dudney Rubie","Beentjes Devin","Baldack Mira","Blunsden Rosalia","Girth Lazaro","Bythway Ennis","Nemchinov Bernete","Thomason Flory","Jenney Carlita","Guwer Alene","Martill Talya","Ralton Venus","Calton Cordelia","Doram Avivah","Prandy Jonathon"]
print("the length of the names list is " + str(len(name_list)))

n = int(input("\n\nenter a number: "))

dict = {}
dictn = {}

#creating a dictionary with numbers
for x in range(0,n):
    dict[x] = x**2
print(dict)

#creating a dictionary with random names
for x in range(0,n):
    dictn[x] = name_list[random.randint(0,len(name_list))]
print(dictn)

print(dictn.keys())



#Grouping word list by first letter

food_list = ["apples","bananas","oranges","carrots","lemons","lollies","cake","cream","milk","mango"]
food_dict = {}

for food in food_list:
    first = food[0]
    if first not in food_dict:
        food_dict[first] = [food]
    else:
        food_dict[first].append(food)

print(food_dict)

#Grouping word list by substring inclusion

contains_dict = {}
contains = input("type your substring...")
in_ = []
out_ = []

for food in food_list:
    if contains in food:
        in_.append(food)
    else:
        out_.append(food)

contains_dict["in"] = in_
contains_dict["out"] = out_

print(contains_dict)



#SLICING LISTS

s_list = []

for i in range(10): #create list with 10 numbers (0-9)
    s_list.append(i)

print(s_list) #give me entire list
print(s_list[:-2]) #give me all but last 2 items
print(s_list[-2:]) #give me only last 2 items
print(s_list[:2]) #give me only first 2 items
print(s_list[2:]) #give me all but first 2


#CREATING SETS

import random

set_list = [2,3,2,2,2,1,2,2,3,1,4,5,6,1,12,23,3,4,1,3,3,31,2,2,2,3,3,4,1,1,1,2,3,4,4,4,12,2,2,2,1]
set1 = set(set_list)

print(sorted(set_list))
print(set1)

set_list2 = []
for x in range(0,20000):
    set_list2.append(random.randint(1,5))

print("set_list2: \n" + str(set_list2))
set2 = set(set_list2)
print(set2)

import re

states = [' Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda', 'south carolina##', 'West virginia?']
dirty_chars = "!@#$%^&*()_+{}|:\"<>?[]\;',./'"


for state in states:

    for x in range(0, len(dirty_chars)):
        state = state.replace(dirty_chars[x],"")

    state = state.rstrip().lstrip().upper()

    print("Name: " + state + " Length: " + str(len(state)))

#BASIC ADDRESS CLEANER

import re

valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
dirty_items  = ['45 geraldino STREAT','100 hund avenue','  ((123 Derrimut lane','12 saddle st',' 13@4$ easy lane','60 toonga road','2., $ gary road','234% denk cres', '%54 JerY rd']
max = 0
clean_items = []

for item in dirty_items:
    if max < len(item):
        max = len(item)

for address in dirty_items:
    for char in address:
        if char not in valid_chars:
            address = address.replace(char, "")

        address = address.strip().upper()

    while "  " in address:
        address = address.replace("  "," ")


    spacer = " || LEN: "

    clean_address = address + spacer + str(len(address))
    clean_items.append(clean_address)

print(clean_items)


#APPEND LINES TO TEXT FILE

my_phrases = []

tries = 1
while tries <= 5:
    phrase = input("Enter a phrase" + " " + str(tries))
    my_phrases.append(phrase)
    tries = tries + 1
print(my_phrases)


x = open("my_list.txt", "a") #appends to text file without deleting existing information, creates file if it does not already exist
try:
    for phrase in my_phrases:
          x.write(phrase)
          x.write("\n")
except:
    print("failed")
else:
    print("success")
finally:
    x.close()

#READING LINES FROM TXT
r = open('my_list.txt' , 'r')

for line in r:
    print("line: " + line)

r.close()

'''