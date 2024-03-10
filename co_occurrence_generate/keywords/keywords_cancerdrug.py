cancerdrug_keywords = [word.lower() for word in [
  #4 
'Abemaciclib', 'LY2835219', 'Verzenio', 'Verzenios', 

#6 
'Abiraterone', 'abiraterone acetate', 'CB7630', 'Abatitor', 'Abione', 'Abiracine', 'Abiracure', 'Abirakast', 'Abiramab', 'Abirapro', 'Abirataj', 'Abiratas', 'Arbitus', 'Ariteron', 'Birato', 'MyTera', 'Samtica', 'Xbira', 'Yonsa', 'Zabiteron', 'Zecyte', 'Zelgor', 'Zybuca', 'Zytiga', 'Zytix', 

#7 
'Acalabrutinib', 'ACP-196', 'Calquence', 

#9 
'Aclarubicin', 'aclacinomycin', 'aclacinomycin A', 'aclacinomycin A hydrochloride', 'aclacinomycin-A', 'aclarubicin hydrochloride', 'MA144-A1', 'Aclacin', 'Aclacinomycine', 'Aclacinon', 'Aclaplastin', 'Jaclacin', 

#12 
'Trastuzumab emtansine', 'ado-trastuzumab emtansine', 'T-DM1', 'TDM1', 'PRO132365', 'Kadcyla', 'Ujvira', 

#13 
'Afatinib', 'afatinib dimaleate', 'BIBW 2992', 'BIBW-2992', 'Afanix', 'Gilotrif', 'Giotrif', 'Tomtovok', 'Tovok', 'Xovoltib', 

#15 
'Aldesleukin', 'IL-2', 'Interleukin-2', 'Macrolin', 'Proleukin', 

#16 
'Alectinib', 'AF-802', 'AF802', 'CH5424802', 'RG7853', 'RO5424802', 'UNII-LIJ4CT1Z3Y', 'Alecensa', 'Alecensaro', 'Alecinix', 'Alecnib', 

#17 
'Alemtuzumab', 'LDP03', 'Campath', 'Campath-1H', 'Lemtrada', 'MabCampath', 

#19 
'Alisertib', 'MLN8237', 

#20 
'All-trans retinoic acid', 'all-trans retinoic acid', 'ATRA', 'tretinoin', 'CA ATRA', 'Ves-ATRA', 'Vesanoid', 

#23 
'Altretamine', 'hexamethylmelamine', 'HMM', 'Hexalen', 'Hexastat', 

#28 
'Aminoglutethimide', 'Aminoblastin', 'Cytadren', 'Elipten', 'Orimentin', 'Orimeten', 'Orimetene', 'Rodazol', 

#29 
'Aminopterin', '4-aminopteroyl-glutamic acid', 

#30 
'Amrubicin', 'AMR', 'amrubicin HCI', 'SM-5887', 'Calsed', 

#31 
'Amsacrine', 'acridinyl anisidide', 'AMSA', "Cain's acridine", 'm-AMSA', 'CI-880', 'SN-11841', 'Amekrin', 'Amsa P-D', 'Amsidine', 'Amsidyl', 'Lamasine', 

#33 
'Anastrozole', 'Altraz', 'Anabrez', 'Anastraze', 'Anastrazol Rontag', 'Anastrol', 'Arimidex', 'Asiolex', 'Karomex', 'Leprofen', 'RUI SI YI', 'RUI Ting', 'Trozolet', 'Trozolite', 

#39 
'Apalutamide', 'ARN-509', 'Erleada', 

#40 
'Apatinib', 'rivoceranib', 'YN968D1', 'Aitan', 

#44 
'Arsenic trioxide', 'Arsenol', 'Arsenox', 'Leusenox', 'Trisenox', 

#45 
'Asparaginase', 'colaspase', 'crisantaspase', 'L Asparaginase', 'L-ASP', 'Asparaginasa', 'Chephacardin', 'Crasnitin', 'Elspar', 'Engenase', 'Kidrolase', 'L Asparaginasa', 'L Asparaginasum', 'L-Asperone', 'L-Ginase', 'Laspar', 'Leucoginase', 'Leunase', 'Onconase', 'Paronal', 'Spectrila', 

#46 
'Asparaginase Erwinia chrysanthemi', 'crisantaspase', 'crisantaspasum', 'Erwinia L-asparginase', 'krisantaspaasi', 'krisantaspas', 'Erwinase', 'Erwinaze', 

#49 
'Atezolizumab', 'MPDL3280A', 'RG7446', 'RO5541267', 'Tecentriq', 

#53 
'Avelumab', 'MSB0010718C', 'Bavencio', 

#54 
'Axicabtagene ciloleucel', 'Axi-cel', 'Axicel', 'KTE-C19', 'Yescarta', 

#55 
'Axitinib', 'AG-013736', 'AG013736', 'Axishil', 'Axpero', 'Inlybest', 'Inlyta', 'Luciax', 

#56 
'Azacitidine', '5-azacitidine', '5-azacytidine', 'Azacitidina', 'Azacytin', 'Azadine', 'Azafect', 'Azaplast', 'Citaza', 'MyAza', 'Myelotex', 'Vidaza', 'Xpreza', 

#59 
'Bacillus Calmette-Guerin', 'Bacille Calmette Guerin', 'TheraCys', 'TICE BCG', 

#61 
'Bavituximab', 'PGN401', 'Tarvacin', 

#63 
'Belinostat', 'PXD101', 'Beleodaq', 

#64 
'Belotecan', 'belotecan hydrochloride', 'CKD-602', 'Camptobell', 

#65 
'Bendamustine', 'bendamustin hydrochloride', 'bendamustine hydrochloride', 'cytostasan hydrochloride', 'CEP-18083', 'SDX-105', 'SyB L-0501', 'Belrapzo', 'Bendamax', 'Bendawel', 'Bendeka', 'Bendit', 'Innomustine', 'Leuben', 'Levact', 'Maxtorin', 'MyMust', 'Purplz', 'Ribomustin', 'Treakisym', 'Treanda', 'Xyotin', 

#68 
'Bevacizumab', 'rhuMab-VEGF', 'Altuzan', 'Avastin', 'BevaciRel', 'Bevarest', 

#69 
'Bexarotene', 'LGD1069', 'Bexgratin', 'Targretin', 

#70 
'Bicalutamide', 'Calutide', 'Casodex', 'Cosudex', 'Kalumid', 

#71 
'Binimetinib', 'ARRY-162', 'ARRY-438162', 'MEK162', 'Mektovi', 

#73 
'Bleomycin', 'Blenoxane', 'Bleo', 'Bleocin', 'Bleocip', 'Bleopar', 'Bleowel', 

#74 
'Blinatumomab', 'AMG 103', 'MEDI538', 'MT103', 'Blincyto', 

#75 
'Bortezomib', 'LDP 341', 'MLN341', 'PS-341', 'Biocure', 'Borater', 'Bortecad', 'Bortemib', 'Bortenat', 'Bortetrust', 'Bortrac', 'Borvex', 'Borviz', 'Botepar', 'Bromadene', 'Egybort', 'Mibor', 'Myezom', 'Norvelzo', 'Ortez', 'Velcade', 'Zomib', 'Zuricade', 

#76 
'Bosutinib', 'SKI-606', 'Bosulif', 

#77 
'Brentuximab vedotin', 'cAC10-vcMMAE', 'SGN-35', 'Adcetris', 

#78 
'Brigatinib', 'AP26113', 'Alunbrig', 'Biganib', 'Briganix', 'Trepmac', 

#79 
'Buparlisib', 'BKM120', 

#80 
'Busulfan', 'Busilvex', 'Busulfex', 'Myleran', 

#81 
'Cabazitaxel', 'RPR116258A', 'TXD258', 'XRP6258', 'Cabapan', 'Cabaxan', 'Cabazither', 'Cabtana', 'Cazat', 'Jevatax', 'Jevtana', 'Kabanat', 'Procabazi', 'Qtervaxia', 'Z-Texel', 

#82 
'Cabozantinib', 'XL-184', 'XL184', 'Cabometyx', 'Caboxen', 'Cabozanib', 'Cabozanix', 'Cometriq', 'Lucicaboz', 

#83 
'Calaspargase', 'calaspargase pegol-mknl', 'Asparlas', 

#86 
'Capecitabine', 'capecitabine RDT', 'kapesitabin', 'Ro 09-1978/000', 'Cabita', 'Capebin', 'Capegard', 'Capnat', 'Caposib', 'Capsy', 'Caxeta', 'Citabin', 'Ecansya', 'Flagoda', 'Naprocap', 'Skemca', 'Xeloda', 'Xlotabin', 

#88 
'Carboplatin', 'JM8', 'Biocarb', 'Biocarbo', 'Bioplatinex', 'Biovinate', 'Blastocarb', 'Bonaplatin', 'Boplatex', 'Carbo', 'Carbokem', 'Carbomedac', 'Carbomerck', 'Carboplat', 'Carboplatine', 'Carboplatino', 'Carboplatinum', 'Carbosin', 'Carbotanil', 'Carbotec', 'Carbotinol', 'Careptin', 'Carplan', 'Carplanil', 'Carpsol', 'CBDCA', 'Crobextin', 'Cycloplatin', 'Cycloplatinum', 'Emorzim', 'Erbakar', 'Ercar', 'Fauldcarbo', 'Ifacap', 'Kemocarb', 'Megaplatin', 'Nealorin', 'Neocarb', 'Neocarbo', 'Oncocarb', 'Paraplatin', 'Paraplatine', 'Pharmaplatin', 'Platamine CS', 'Platinwas', 'Ribocarbo', 'Tecnocarb', 'Vancel', 

#89 
'Carfilzomib', 'CFZ', 'PR-171', 'Carfilnat', 'Kyprolis', 

#90 
'Carmustine', 'BCNU', 'bischloroethylnitrosourea', 'carmustin', 'Becenun', 'BiCNU', 'Carmubris', 'Leucerom', 'Nitrourean', 'Nitrumon', 

#91 
'Carmustine wafer polifeprosan 20', 'polifeprosan 20 with carmustine implant', 'NPC-08', 'NSC-409962', 'WR-139021', 'Biodel', 'Gliadel wafer', 

#94 
'Cediranib', 'AZD2171', 'Recentin', 

#95 
'Cemiplimab', 'cemiplimab-rwlc', 'REGN2810', 'Libtayo', 

#96 
'Ceritinib', 'LDK378', 'Lucicer', 'Noxalk', 'Spexib', 'Zykadia', 

#98 
'Cetuximab', 'C225', 'Cetuxim', 'Erbitux', 

#99 
'Chidamide', 'tucidinostat', 'CS055', 'HBI-8000', 'Epidaza', 

#100 
'Chlorambucil', 'Chlorambusil', 'Chloraminophene', 'Chlorbutin', 'Chlorobutin', 'Leukeran', 'Linfoxan', 

#105 
'Cisplatin', 'CDDP', 'cis-diamminedichloroplatinum III', 'cis-platinum', 'cisplatinum', 'DACP', 'DDP', 'NSC 119875', 'Abiplatin', 'Axiplat', 'Biocisplatinum', 'Bioplatino', 'Blastolem', 'Briplatin', 'Brisplatin', 'C-Platin', 'Ceplatin', 'Ciplatan', 'Ciplexal', 'Cis-GRY', 'Cismaplat', 'Cispatin', 'Cisplamerck', 'Cisplan', 'Cisplasol', 'Cisplatex', 'Cisplatine', 'Cisplatino', 'Cisplatyl', 'Cisteen', 'Citoplatino', 'Citosin', 'Cysplatyna', 'Cytoplatin', 'Docistin', 'Elvecis', 'Fauldcispla', 'Ifapla', 'Kemoplat', 'Lederplatin', 'Metaplatin', 'Neoplat', 'Neoplatin', 'Noveldexis', 'Oncoplatin AQ', "Peyrone's Chloride", "Peyrone's Salt", 'Placis', 'Plastistil', 'Platamin', 'Platamine', 'Platiblastin', 'Platicis', 'Platidiam', 'Platikem', 'Platil', 'Platimit', 'Platin', 'Platinex', 'Platinil', 'Platino II Filaxis', 'Platinol', 'Platinox', 'Platinoxan', 'Platiran', 'Platistil', 'Platistin', 'Platistine', 'Platosin', 'Randa', 'Romcis', 'Sicatem', 'Sinplatin', 'Sisplanil', 'Tecnoplatin', 'Tisplal', 'Unistin', 

#107 
'Cladribine', '2-CdA', '2-chlorodeoxyadenosine', 'Leustatin', 'Litak', 'Movectro', 

#108 
'Clarithromycin', 'Biaxin', 

#111 
'Clofarabine', 'klofarabin', 'Clolar', 'Evoltra', 'Evorabin', 'Ivozall', 

#113 
'Cobimetinib', 'GDC-0973', 'XL518', 'Cotellic', 

#115 
'Copanlisib', 'BAY 80-6946', 'Aliqopa', 

#116 
'Cortisone', 

#119 
'Crizotinib', 'PF-02341066', 'PF02341066', 'Crizalk', 'Crizocap', 'Crizonix', 'Xalkori', 

#122 
'Cyclophosphamide', 'CP monohydrate', 'CPM', 'cyclophosphamid monohydrate', 'cyclophosphamide monohydrate', 'Asta B 518', 'B-518', 'WR-138719', 'Alkyloxan', 'Biodoxan', 'Carloxan', 'Ciclofosfamida', 'Ciclokebir', 'Cicloxal', 'Clafen', 'Claphene', 'Cyclam', 'CYCLO-cell', 'Cycloblastin', 'Cycloblastine', 'Cycloferon', 'Cyclomide', 'Cyclophar', 'Cyclophospham', 'Cyclophosphamid', 'Cyclophosphane', 'Cyclostin', 'Cyclostine', 'Cyclotox', 'Cycloxan', 'Cycram', 'Cydoxan', 'Cyklofosfamid', 'Cyphos', 'Cytophosphan', 'Cytoxan', 'Cytoxan Lyophilized', 'Endoxan', 'Endoxan-N', 'Endoxana', 'Enduxan', 'Formitex', 'Fosfaseron', 'Genoxal', 'Genuxal', 'Hidrofosmin', 'Ledoxan', 'Ledoxina', 'Mitoxan', 'Neophos', 'Neosar', 'Oncomide', 'Oncophos', 'Procytox', 'Revimmune', 'Sendoxan', 'Siklofos', 'Syklofosfamid', 'Tymtran', 'Zuviphos', 'Zycram', 'Zytoxan', 

#125 
'Cyproterone acetate', 'Androcur', 

#126 
'Cytarabine', 'Ara-C', 'arabinofuranosyl cytidine', 'arabinosylcytosine', 'cytosine arabinoside', 'Alcysten', 'Alexan', 'ARA', 'Arabine', 'Arabitin', 'Aracitin', 'Aracytin', 'Aracytine', 'Citagenin', 'Citaloxan', 'Citarabin', 'Citarabina', 'Citarabins', 'Citarax', 'Cylocide', 'Cytarabin', 'Cytarabins', 'Cytarabinum', 'Cytarbel', 'Cytarine', 'Cytosar', 'Cytosar-U', 'Cytrosar', 'Depocyt', 'Depocyte', 'Erbabin', 'Erpalfa', 'Fauldcita', 'Groven', 'Ifarab', 'Iretin', 'Laracit', 'Medsara', 'Novutrax', 'Remcyta', 'Starasid', 'Tabin', 'Tabine', 'Udicil', 

#127 
'Cytarabine and daunorubicin liposomal', 'CPX-351', 'Vyxeos', 'Vyxeos liposomal', 

#131 
'Dabrafenib', 'dabrafenib mesylate', 'GSK-2118436A', 'GSK2118436', 'Rafinlar', 'Tafinlar', 

#132 
'Dacarbazine', 'dacarbazin', 'DTIC', 'imidazole carboxamide', 'Bazipar', 'Cedcozine', 'Dacarba', 'Dacarex', 'Dacin', 'Dacmed', 'Darbazine', 'Dazine', 'Decarb', 'Oncodac', 'Zydac', 

#133 
'Dacomitinib', 'PF-00299804', 'Vizimpro', 

#134 
'Dactinomycin', 'AC-DE', 'actinomycin D', 'Cosmegen', 'Dacmozen', 'Lyovac', 

#137 
'Danazol', 'Danatrol', 'Danocrine', 'Danodiol', 'Danogen', 'Drane', 'Ladogal', 'Novaprin', 

#139 
'Daratumumab', 'daratumumab-fihj', 'JNJ-54767414', 'Darzalex', 'HuMax-CD38', 

#141 
'Darolutamide', 'BAY-1841788', 'ODM-201', 'Nubeqa', 

#142 
'Dasatinib', 'BMS-354825', 'Sprycel', 

#143 
'Daunorubicin', 'daunomycin', 'Cerubidin', 'Cerubidine', 'D-Blastin', 'Daunoblastin', 'Daunoblastina', 'Daunocin', 'Daunomicina', 'Daunorubicine', 'Daurocina', 'Maxidauno', 'Ondena', 'Rubidomycin', 'Rubilem', 'Rubomycin', 'Runabicon', 

#144 
'Daunorubicin liposomal', 'daunorubicin citrate liposome injection', 'DaunoXome', 

#145 
'Decitabine', "5-aza-2'-deoxycytidine", 'Dacogen', 'Decima', 'Decita', 'Decitafect', 'Decitas', 'Decitex', 'Natdecita', 

#151 
'Degarelix', 'degarelix acetate', 'ASP3550', 'FE200486', 'Firmagon', 

#152 
'Denileukin diftitox', 'DAB(389)-interleukin-2', 'DAB389 interleukin-2', 'DAB389 interleukin-2 immunotoxin', 'DABIL2', 'LY335348', 'Ontak', 

#154 
'Denosumab', 'Prolia', 'Xgeva', 

#156 
'Dexamethasone', 'dexamethasone acetate', 'dexamethasone sodium', 'dexamethasone sodium metasulfobenzoate', 'dexamethasone sodium phosphate', 'dexamethasone sodium succinate', 'dexamethasone sodium sulfate', 'Aacidexam', 'Acetato DE Dexametasona', 'Acetazona', 'Acolon', 'Adrecort', 'Adrekon', 'Aeroseb-DEX', 'Afpred Forte-Dexa', 'AK-DEX', 'Aldron', 'Alfalyl', 'Alpermell', 'Amumetazon', 'Anemul', 'Aphtasolon', 'Apidex', 'Arcodexan', 'Auxiloson', 'Auxison', 'Auxisone', 'B Dexzol', 'Baycadron', 'Bexine', 'Beyonas Dexa', 'Bisuo DS', 'Brulin', 'Bucokon', 'Bufadexon', 'Butiol', 'Canalon', 'Carbidu', 'Carulon', 'Cebedex', 'Cellacort', 'Celudex', 'Cetadexon', 'Colircusi Dexametasona', 'Corodex', 'Corson', 'Corsona', 'Corsone', 'Corsum', 'Corticoidex', 'Cortidax', 'Cortidex', 'Cortidexason', 'Cortitop', 'Coyensu', 'D-Cort', 'Dacrosone', 'Daidoron', 'Dalalone', 'Danason', 'Danasone', 'Daxilone', 'Deca Forte', 'Decacin', 'Decaderm', 'Decadolone', 'Decadran', 'Decadron', 'Decadronal', 'Decadronfosfat', 'Decafos', 'Decalin', 'Decalon', 'Decalona', 'Decan', 'Decans', 'Decaron', 'Decason', 'Decasone', 'Decaspray', 'Decazol', 'Decdak', 'Decdan', 'Decicort', 'Decilone', 'Decobel', 'Decolite', 'Decone', 'Decordex', 'Decorex', 'Decoron', 'Decorten', 'Dectan', 'Dectancyl', 'Deexa', 'Deflaren', 'Dekesu', 'Dekisachosei', 'Dekort', 'Deksa', 'Deksalon', 'Deksamet', 'Dellamethasone', 'Deltafluorene', 'Demasone', 'Demeson', 'Dermadex', 'Dermidron', 'Deron S', 'Deronil', 'Derson', 'Dersone', 'Desalark', 'Desametasone Fosf', 'Desason', 'Deson', 'Detametazon', 'Detasone', 'Dethamedin', 'Dexa', 'Dexa Clinit', 'Dexabene', 'Dexabeta', 'Dexacen-4', 'Dexacilin', 'Dexacip', 'Dexacollyre', 'Dexacom', 'Dexacort', 'Dexacortal', 'Dexacortin', 'Dexacortisone', 'Dexacortisyl', 'Dexacotsil', 'Dexacron', 'Dexacutis', 'Dexaden', 'Dexaderm', 'Dexaderme', 'Dexadermil', 'Dexadon', 'Dexadrol', 'Dexadron', 'Dexaedo', 'Dexafar', 'Dexafarm', 'Dexaflam', 'Dexaflan', 'Dexagalen', 'Dexagee', 'Dexagel', 'Dexagenta', 'Dexaglos', 'Dexagreen', 'Dexagrin', 'Dexahexal', 'Dexaleniens', 'Dexalocal', 'Dexaltin', 'Dexam', 'Dexamag', 'Dexamark', 'Dexame', 'Dexamecortin', 'Dexamedis', 'Dexamedix', 'Dexamedron', 'Dexameral', 'Dexameson', 'Dexamesone', 'Dexamet', 'Dexametason', 'Dexametasona', 'Dexametax', 'Dexametazon', 'Dexametazona', 'Dexameth', 'Dexamethason', 'Dexamethasonum', 'Dexamethazon', 'Dexamethazone', 'Dexametin', 'Dexametisona', 'Dexametonal', 'Dexametrat', 'Dexamex', 'Dexamil', 'Dexamine', 'Dexaminor', 'Dexamo', 'Dexamonozon N', 'Dexan', 'Dexanel', 'Dexanil', 'Dexano', 'Dexaphos', 'Dexapolcort', 'Dexapro', 'Dexaril', 'Dexaroid', 'Dexaron', 'Dexart', 'Dexasin', 'Dexasine', 'Dexasol', 'Dexasolone', 'Dexason', 'Dexasone', 'Dexasonlin', 'Dexatab', 'Dexaton', 'Dexatop', 'Dexatotal', 'Dexaval', 'Dexaven', 'Dexavet', 'Dexawal', 'Dexawieb', 'Dexazen', 'Dexazona', 'Dexazone', 'Dexicorta', 'Dexin', 'Dexinga', 'Dexion', 'Dexmene', 'Dexmesone', 'Dexmetha', 'Dexmethasone', 'Dexmethsone', 'Dexona', 'Dexone', 'Dexonium', 'Dexoptic', 'Dexpak', 'Dexsol', 'Dexstar', 'Dextason', 'Dexthasol', 'Dexton', 'Dextrasone', 'Dicorsone', 'Dicosheun', 'Diometa', 'Dison', 'DM Solone', 'Donray', 'Dorison', 'Doronil', 'Drenex', 'Drxaline', 'Elixirmethasone', 'Epidexone', 'Epidrone', 'Erladexone', 'Ermethasone', 'ETA Cortilen', 'Etason', 'Euromethasone', 'Fada Dexametasona', 'Fadametasona', 'Faridexon', 'Fexadron', 'Fortecortin', 'Fosfato Dissodico Dexametasona', 'Gammacorten', 'Gemisona', 'Glymesason', 'Grathazon', 'Hexadecadrol', 'Hexadrol', 'HI-Methasone', 'Hopamethasone', 'Idizone', 'Indexon', 'Inthesa-5', 'Irzamethazone', 'Isodexam', 'Isopto', 'Kaarmepakkaus', 'Kalmethasone', 'Kanadex', 'Kodolo', 'Kosa', 'Kovintong', 'Lanadexon', 'Licoson', 'Limethason', 'Lipotalon', 'Lisoderme', 'Lodex', 'Lodexa', 'Lokalison-F', 'Lormine', 'Loverine', 'Lupidexa', 'Luxazone', 'Maradex', 'Maxidex', 'Mecoxon', 'Medesone', 'Medexasone', 'Mediamethasone', 'Medicort', 'Medidex', 'Megacort', 'Megadex', 'Mephameson', 'Mephamesona', 'Mephamesone', 'Mephamesone-4', 'Meradexon', 'Merideca', 'Mesadoron', 'Metalexina', 'Metasolon', 'Metax', 'Metaxon', 'Metcort', 'Methaderm', 'Methasone', 'Mexasone', 'Mexaton', 'Migradexan', 'Millicorten', 'Minidex', 'Mitasone', 'Molacort', 'Mycidex', 'Neodex', 'Neofordex', 'Nexadron', 'Nodevex', 'Nufadex M', 'Ocedran', 'Ocudex', 'Oftadek', 'Oftadex', 'Omedexon', 'Onadron', 'Ophth-DEX', 'Ophthasona', 'Opticort', 'Orazone', 'Ordex', 'Orgadrone', 'Penatone', 'Penodex', 'Phenodex', 'Pidexon', 'Plavex', 'Plidexa', 'Prodexon', 'Pyderma', 'Pyradexon', 'Rally-A', 'Randexa', 'Redexon', 'Rednisone', 'Reusan', 'Rocolone', 'Ronic', 'Roximeth', 'Rupedex', 'Santeson', 'Sawasone', 'Scandexon', 'Selftison', 'Shirodex', 'Shuayan', 'Smile', 'Solcort', 'Soldesam', 'Soldesanil', 'Soldex', 'Soludecadron', 'Solupen', 'Sonexa', 'SP Cordexa', 'Spersadex', 'Spondy-Dexa', 'Stedex', 'Steralol', 'Sterasone', 'Steron', 'Superprednol', 'Supertendin-Depot N', 'Suprason', 'Surodex', 'Sydencort', 'Syndexa', 'Tavesona', 'Teanlang', 'Teikason Nidek', 'Tekuron', 'Thilodex', 'Thilodexine', 'Totocortin', 'Tuttozem N', 'Ucalon', 'Udicort', 'Unidex', 'Unidexa', 'Unisone', 'Visualin', 'Visumetazone', 'Voalla', 'Windex', 'Wymesone', 'Xasone', 'Xine', 'Zalucs', 'Zecaxon', 'Zenos', 'ZoDex', 'Zydexa', 

#158 
'Dexrazoxane', 'dexrazoxane hydrochloride', 'ADR-529', 'ICRF-187', 'Cardioxane', 'Cyrdanax', 'Savene', 'Totect', 'Zinecard', 

#159 
'Diethylstilbestrol', 'DES', 'stilbestrol', 'stilboestrol', 'Desplex', 'Dibestrol', 'Stibrol', 'Stilbest', 

#161 
'Dinutuximab', 'Ch14.18', 'MOAB Ch14.18', 'monoclonal antibody Ch14.18', 'Unituxin', 

#164 
'Docetaxel', 'NSC 628503', 'RP 56976', 'Asodocel', 'Daxotel', 'Docefrez', 'Docegem', 'Doceglob', 'Docemax', 'Docenat', 'Docepar', 'Docetax', 'Docetec', 'Docetere', 'DoceXan', 'Docshil', 'Dolectran', 'Doxel', 'Doxetal', 'Hentaxel', 'Neocel', 'Oncodocel', 'Plustaxano', 'Sibatere', 'Taceedo', 'Taxe-RTU', 'Taxespira', 'Taxewell', 'Taxotere', 'Texot', 'Trixotene', 'Uvtere', 

#169 
'Doxifluridine', 'Didox', 

#170 
'Doxorubicin', 'ADM', 'doxorubicin hydrochloride', 'hydroxydaunorubicin', 'FI-106', 'Adriablastina', 'Adriacept', 'Adriacin', 'Adriamycin', 'Adriamycine', 'Adriblastin', 'Adriblastina', 'Adriblastine', 'Adricept', 'Adricin', 'Adrim', 'Adrimedac', 'Adrosal', 'Antraciclin', 'Biorrub', 'Biorubina', 'Cadria', 'Carcinocin', 'Cloridrato DE', 'Deldoxin', 'Dicladox', 'Dobicin', 'Dobixin', 'Doxo', 'Doxo Cell', 'Doxobin', 'Doxocris', 'Doxokebir', 'Doxolem', 'Doxonolver', 'Doxor', 'Doxorrubicina', 'Doxorrubicina Colhidrol', 'Doxoruben', 'Doxorubicina', 'Doxorubicine', 'Doxorubicinum', 'Doxorubin', 'Doxotec', 'Doxtie', 'Duxocin', 'Evacet', 'Farmiblastina', 'Fauldoxo', 'Flavicina', 'Ifadox', 'Kemodoxa', 'Lyphidox', 'Nagun', 'Neoxane', 'Nuaze', 'Oncodria', 'Onkodox', 'Onkostatil', 'Pallagicin', 'Ranxas', 'Rastocin', 'Ribodoxo', 'Roxorin', 'Rubex', 'Varidoxo', 'Zodox', 

#171 
'Doxycycline', 

#173 
'Durvalumab', 'MEDI4736', 'Imfinzi', 

#174 
'Dutasteride', 'Avodart', 

#175 
'Duvelisib', 'IPI-145', 'Copiktra', 

#178 
'Edrecolomab', 'Panorex', 

#179 
'Elotuzumab', 'anti-CS1 monoclonal antibody HuLuc63', 'BMS-901608', 'HuLuc63', 'PDL-063', 'PDL063', 'Empliciti', 

#182 
'Enasidenib', 'enasidenib mesylate', 'AG-221', 'CC-90007', 'Idhifa', 

#183 
'Encorafenib', 'LGX818', 'Braftovi', 

#188 
'Entrectinib', 'RXDX-101', 'Rozlytrek', 

#189 
'Enzalutamide', 'MDV3100', 'Azel', 'Bdenza', 'Bnyx', 'Capmide', 'Enzamide', 'Glenza', 'Indenza', 'Xtandi', 

#191 
'Epirubicin', '4-epi-doxorubicin', 'epidoxorubicin', 'Alrubicin', 'Anthracin', 'Binarin', 'Bioepicyna', 'Crisabon', 'E.P.R Elvetium', 'Ellence', 'Epidoxo', 'Epifil', 'Epilem', 'Epirubicine', 'Epizin', 'Epricin', 'Eracin', 'Famorubicin', 'Farmorubicin', 'Farmorubicina', 'Farmorubicine', 'Pharmorubicin', 'Riboepi', 'Rubifarm', 

#196 
'Erdafitinib', 'JNJ-42756493', 'Balversa', 

#197 
'Eribulin', 'eribulin mesylate', 'E7389', 'ER-086526', 'NSC-707389', 'Brutravon', 'Ebunat', 'Epbriv', 'Halaven', 'Mitobulin', 'Rayldeima', 'Teceris', 

#198 
'Erlotinib', 'erlotinib hydrochloride', 'CP-358', 'CP-774', 'OSI-774', 'Erlocip', 'Erlonat', 'Melacyte', 'Tarceva', 

#199 
'Estradiol', 'estradiol valerate', 'estrogens conjugated', 'estrogens esterified', 

#200 
'Estramustine', 'estramustine phosphate sodium', 'Emcyt', 'Estracit', 'Estram', 'Estramin', 'X-Trant', 

#201 
'Etoposide', 'etoposide phosphate', 'VP 16213', 'VP-16', 'VP-TEC', 'Aside', 'Beposid', 'Bioposide', 'Celltop', 'Citodox', 'Epocin', 'Eposid', 'Eposide', 'Eposido', 'Eposin', 'Epsidox', 'ETO', 'Etocris', 'Etomedac', 'Etonolver', 'Etopofos', 'Etopophos', 'Etopos', 'Etoposid', 'Etoposido', 'Etopoxan', 'Etopul', 'Etosid', 'Etosin', 'Eunades CS', 'Euvaxon', 'Exitop', 'Fytop', 'Fytosid', 'Labimion', 'Lastet', 'Lastet S', 'Neoplaxol', 'Nexvep', 'Onkoposid', 'Optasid', 'Percas', 'Posid', 'Posidon', 'Posyd', 'Riboposid', 'Sintopozid', 'Toposar', 'Toposide', 'Toposin', 'Topresid', 'Tosuben', 'Vepefos', 'Vepesid', 'Vepeside', 'Vepsid', 'Vepside', 

#202 
'Everolimus', 'RAD-001', 'RAD001', 'Advacan', 'Afinitor', 'Afinitor Disperz', 'Certican', 'Everecan', 'EverGraf', 'Evermil', 'Evertor', 'Rapact', 'Rolimus', 'Votubia', 'Zortress', 

#203 
'Exemestane', 'FCE-24304', 'Aromadex', 'Aromasin', 'Aromex', 'Xtane', 

#222 
'Floxuridine', 'floxuridin', 'fluorodeoxyuridine', 'fluorouridine deoxyribose', 'WR-138720', 'FUDR', 

#224 
'Fludarabine', 'FAMP', 'fludarabine phosphate', 'Beneflur', 'Fludabine', 'Fludara', 'Lymfuda', 'Oforta', 

#225 
'Fluorouracil', '5 Fluorouracil', '5 FU', '5-fluoracilo', '5-fluorouracilo', '5-fluorouracyl', '5-FU', 'FU', 'Ro-2-9757', 'Accusite', 'Actino Hermal', 'Adrucil', 'Arumel', 'Benton', 'Biofur', 'Carac', 'Carebin', 'Carzonal', 'Cinco-FU', 'Cinkef-U', 'Curacil', 'Effcil', 'Efudex', 'Efurix', 'Ezadex', 'Fauldfluor', 'Fivocil', 'Fivoflu', 'Flacule', 'Flonida', 'Florac', 'Fluhomer', 'Fluolex', 'Fluor-Uracil', 'Fluoro-Uracil ICN', 'Fluoro-Uracile ICN', 'Fluoroplex', 'Fluorouracile', 'Fluorouracilo', 'Fluorourcil', 'Fluoruracilo', 'Fluoxan', 'Flurablastin', 'Flurac', 'Fluracedyl', 'Fluracil', 'Fluril', 'Fluroblastin', 'Fluroblastine', 'Ftoruracil', 'Ftouracil', 'Haemato-FU', 'Ifacil', 'Kang Ning', 'Kecimeton Tatumi', 'Killit', 'Lunachol', 'Lunapon', 'Natira U', 'Neofluor', 'O Fluor', 'Oncofu', 'Onkofluor', 'Pentafu', 'Pharmauracil', 'Phthoruracil', 'Phtoruracil', 'Ribofluor', 'Rotianin', 'Satelol', 'Seco Uracil', 'Tecflu', 'Timadin', 'Triosules', 'Uflahex', 'Ulosagen', 'Ulup', 'Uraciflor', 'Utoral', 'Vaflu', 'Vafu', 

#226 
'Fluoxymesterone', 'Halotestin', 'Ultandren', 

#227 
'Flutamide', 'Cytomid', 'Euflex', 'Eulexin', 'Flutamid', 'Flutatec', 'Lutamide', 'Proscan', 'Tamid', 

#229 
'Folinic acid', 'calcium folinate', 'citrovorum factor', 'folinate calcium', 'folinato de calcio', 'leucovorin calcium', 'LV', 'sodium folinate', 'Antrex', 'Asovorin', 'Biovorin', 'Buateron', 'Calc Leucovorn', 'Calcifolin', 'Calcium Folinato', 'Calcium Folint', 'Calcium Leucovorin', 'Calcium Leucovorn', 'Calciumfolin', 'Calciumfolinat', 'Calcivoran', 'Calfolex', 'Calfolin', 'Calinat', 'Cehafolin', 'Citofolin', 'Claro', 'Cromatonbic Folinico', 'Dalisol', 'Degalin', 'Divifolin', 'Durofolin', 'Ecofol', 'Elvefocal', 'Emovis', 'Erbanfol', 'Estroquin', 'Fastovorin', 'Fauldleuco', 'Fayining', 'Fedolen', 'Ferbon', 'Folaren', 'Folaxin', 'Foli Cell', 'Foliben', 'Folidan', 'Folidar', 'Foliment', 'Folinac', 'Folinato', 'Folinfabra', 'Folinoral', 'Folinoxan', 'Folinvit', 'Foliplus', 'Folmigor', 'Ifavor', 'Isovorin', 'Kalciumfolinat Perivita', 'Kalsiumfolinat', 'Kunyrin', 'Lederfolat', 'Lederfolin', 'Lederfoline', 'Ledervorin', 'Legifol', 'Leucocalcin', 'Leuconolver', 'Leucosar', 'Leucovorin', 'Leucovorina', 'Leucovorine', 'Leukovorin', 'Lovorin', 'Medicofolin', 'Medifolin', 'Medsavorina', 'Neofolin', 'Nyrin', 'O Folin', 'Osfolate', 'Osfolato', 'Perfolate', 'Prefolic', 'Prevax', 'Recovorin', 'Reotan', 'Rescuvolin', 'Resfolin', 'Ribofolin', 'Rontafor', 'Sanifolin', 'Tecnovorin', 'Tonofolin', 'Veravorin', 'Vorina', 'Wellcovorin', 'Zyofolin', 'Zytofolin', 

#231 
'Formestane', 'Lentaron', 

#232 
'Forodesine', 'immucillin H', 'BCX-1777', 'Fodosine', 'Mundesine', 

#234 
'Fostamatinib', 'R788', 'R935788', 'Tavalisse', 'Tavlesse', 

#235 
'Fotemustine', 'Muphoran', 'Mustophoran', 

#237 
'Fulvestrant', 'ICI 182780', 'ZD9238', 'Faslodex', 'Fasnorm', 'Fulvenat', 'Fulvidax', 'Fuvestrol', 

#240 
'Ganetespib', 'STA-9090', 

#242 
'Gefitinib', 'ZD1839', 'Cangib', 'Denrit', 'Geffy', 'Gefitec', 'Gefitero', 'Gefonib', 'Geftib', 'Geftican', 'Gefticip', 'Geftilon', 'Geftinat', 'Geftiwel', 'Iressa', 'KabiGef', 

#243 
'Gemcitabine', 'difluorodeoxycytidine hydrochloride', 'gemcitabine hydrochloride', 'LY-188011', 'Gemcite', 'Gemzar', 'Infugem', 

#244 
'Gemtuzumab ozogamicin', 'Mylotarg', 

#245 
'Gilteritinib', 'ASP2215', 'Xospata', 

#246 
'Glasdegib', 'PF-04449913', 'Daurismo', 

#248 
'Goserelin', 'goserelin acetate', 'Novgos', 'Zoladex', 

#256 
'Histrelin', 'histrelin acetate', 'Supprelin', 'Vantas', 

#258 
'Hydrocortisone', 'hydrocortisone sodium phosphate', 'hydrocortisone sodium succinate', 'Cortef', 

#259 
'Hydroxyurea', 'dhnp', 'hidroxiurea', 'hydroxycarbam', 'hydroxycarbamid', 'hydroxycarbamide', 'Biosupressin', 'Cytodrox', 'Droxia', 'Droxiurea', 'Durea', 'Hidrea', 'Hondrea', 'Hydab', 'Hydrea', 'Hydrine', 'Hydrourea', 'Hytas', 'Litalir', 'Myelostat', 'Mylocel', 'Neodrea', 'Onco Carbide', 'Siklos', 'Syrea', 'Ureax', 'Xromi', 

#262 
'Ibritumomab tiuxetan', 'Zevalin', 

#263 
'Ibrutinib', 'CRA-032765', 'PCI-32765', 'Ibrunib', 'Ibrutix', 'Imbruvica', 'Lucibru', 

#264 
'Icotinib', 'BPI-2009H', 'Conmana', 

#265 
'Idarubicin', 'idarubicin comp', 'idarubicin hydrochloride', 'Idamycin', 'Idaru', 'Ondarubin', 'Zavedos', 'Zavedose', 

#267 
'Idelalisib', 'CAL-101', 'GS 1101', 'GS-1101', 'Zydelig', 

#268 
'Ifosfamide', 'Alquimid', 'Duvaxan', 'Fentul', 'Fosfidex', 'Haloxan', 'Holoxan', 'Holoxane', 'Ifex', 'IFO Cell', 'Ifocris', 'Ifolem', 'Ifomida', 'Ifomide', 'Ifos', 'Ifosfamida', 'Ifoxan', 'IFX', 'Ipamide', 'Isophosphamide', 'Isoxan', 'Macdafen', 'Mitoxana', 'Tronoxal', 

#269 
'Imatinib', 'imatinib mesilate', 'imatinib mesylate', 'CGP 57148', 'CGP57148B', 'STI-571', 'Enliven', 'Gleevac', 'Gleevec', 'Glivec', 'Imalek', 'Imatib', 'Temsan', 'Veenat', 

#272 
'Infigratinib', 'BGJ398', 'Truseltiq', 

#273 
'Inotuzumab ozogamicin', 'CMC-544', 'Besponsa', 

#274 
'Interferon alfa-2a', 'Laroferon', 'Roferon-A', 

#275 
'Interferon alfa-2b', 'Advaferon', 'Alfaferone', 'Biogamma', 'Canferon A', 'Cytoferon', 'Egiferon', 'Feron', 'Fiblaferon', 'Finnferon-Alpha', 'Frone', 'Heberon Alfa R', 'Humoferon', 'IFN Alpha', 'Imufor', 'Imukin', 'INF', 'Inferax', 'Infergen', 'Inmutag', 'Interfero', 'Interferon Alfanative', 'Interferon Human', 'Interferon Leucocyticum', 'Interferon Lymphoblastoid', 'Interferonum Leucocyticum', 'Intron-A', 'IntronA', 'Multiferon', 'Namalvin', 'OIF', 'Polyferon', 'Realdiron', 'Roceron-A', 'Sumiferon', 

#276 
'Interferon gamma-1b', 'Actimmune', 

#279 
'Ipilimumab', 'BMS-734016', 'MDX-010', 'Yervoy', 

#280 
'Irinotecan', 'Camptothecin-11', 'CPT-11', 'U-101440E', 'Axinotecan', 'Biotecan', 'Biskam', 'Campostar', 'Campto', 'Camptosar', 'Elinatecan', 'Faultenocan', 'Irenax', 'Irinogen', 'Irinomedac', 'Irinotel', 'Irinotesin', 'Irnocam', 'Itoxaril', 'Linatecan', 'Satigene', 'Tecnotecan', 'Tekamen', 'Toptecin', 'Trinotecan', 'Winol', 

#281 
'Irinotecan liposome', 'MM-398', 'MM398', 'PEP-02', 'PEP02', 'Onivyde', 'Onivyde pegylated liposomal', 

#284 
'Isatuximab', 'isatuximab-irfc', 'SAR-650984', 'Sarclisa', 

#285 
'Isotretinoin', '13-cis-retinoic acid', '13-cis-vitamin A acid', '13-CRA', 'cis-retinoic acid', 'isotretinoinum', 'neovitamin A', 'Ro 4-3780', 'Absorica', 'Accure', 'Accutane', 'Amnesteem', 'Cistane', 'Claravis', 'Isotrex', 'Isotrexin', 'Myorisan', 'Oratane', 'Roaccutan', 'Roaccutane', 'Roacutan', 'Sotret', 'Zenatane', 

#287 
'Ivosidenib', 'AG-120', 'Tibsovo', 

#288 
'Ixabepilone', 'azaepothilone B', 'epothilone B lactam', 'BMS-247550', 'Ixempra', 

#289 
'Ixazomib', 'MLN2238', 'MLN9708', 'Ninlaro', 

#290 
'Ketoconazole', 'Nizoral', 

#294 
'Lanreotide', 'lanreotide acetate', 'Ipstyl', 'Lanreotide Autogel', 'Somatuline', 'Somatuline Autogel', 'Somatuline Depot', 'Somatuline LA', 'Somatuline LP', 'Somatuline PR', 

#295 
'Lansoprazole', 'Prevacid', 

#296 
'Lapatinib', 'GW572016', 'Abnib', 'Combinib', 'Etibo', 'Herduo', 'Herlapsa', 'Hertab', 'Lapanix', 'Lapatem', 'Tykerb', 'Tyverb', 

#298 
'Larotrectinib', 'LOXO-101', 'Vitrakvi', 

#299 
'Lenalidomide', 'CC-5013', 'IMiD-1', 'NSC-703813', 'Adlinod', 'Immunomide', 'Kabillon', 'Lenalid', 'Lenalidomid', 'Lenangio', 'Lenmid', 'Lenome', 'Lenomust', 'Lenzest', 'Lidmed', 'Linamide', 'Lynide', 'MyeloSar', 'Revlimid', 

#300 
'Lenograstim', 'Granocyte', 'Neutrogin', 

#301 
'Lenvatinib', 'E7080', 'Kisplyx', 'Lenvima', 

#304 
'Letrozole', 'CGS 20267', 'Femara', 'Fempro', 'Gynotril', 'Latrotal', 'Lerozol', 'Letoval', 'Letpro', 'Letromina', 'Letroplex', 'Letroz', 'Letrozol', 'Lexel', 'Lezole', 

#305 
'Leuprolide', 'leuprolide acetate', 'leuprorelin', 'leuprorelin acetate', 'A-43818', 'TAP-144', 'Camcevi', 'Carcinil', 'Depo-Eligard', 'Eligard', 'Enanton', 'Enantone', 'Enantone-Gyn', 'Ginecrin', 'Leuplin', 'Leupromer', 'Leuprorelin', 'Leuren', 'Lorelin Depot', 'Lucrin', 'Lucrin Depot', 'Lupard Depot', 'Lupoide Depot', 'Lupride Depot', 'Luprodex Depot', 'Lupron', 'Lupron Depot', 'Procren', 'Procrin', 'Prostap', 'Trenantone', 'Uno-Enantone', 'Valeuprox', 'Viadur', 

#306 
'Levamisole', 'Ergamisol', 

#308 
'Levoleucovorin', 'levoleucovorin calcium', 'Fusilev', 

#311 
'Lomustine', 'CCNU', 'CeeNu', 'Gleostine', 

#314 
'Lorlatinib', 'PF-06463922', 'Lorbrena', 'Lorviqua', 

#316 
'Lutetium Lu 177 dotatate', 'Lutathera', 

#318 
'Tafasitamab', 'tafasitamab-cxix', 'MOR00208', 'MOR208', 'XmAb5574', 'Minjuvi', 'Monjuvi', 

#322 
'Mechlorethamine', 'chlormethine', 'nitrogen mustard', 'Ledaga', 'Mustargen', 'Mustine', 

#323 
'Medroxyprogesterone', 'medroxyprogesterone acetate', 'MPA', 'Depo-Provera', 'Provera', 

#324 
'Megestrol', 'megestrol acetate', 'SC10363', 'Maygace', 'Megace', 'Megestat', 'Megestil', 'Niagestin', 'Ovaban', 'Pallace', 

#325 
'Melphalan', 'L-PAM', 'L-Sacrolysin', 'L-Sarcolysin', 'MPL', 'phenylalanine mustard', 'Alkeran', 'Alkerana', 'Evomela', 'Levofolan', 'Melfalan', 'Phelinun', 

#327 
'Mercaptopurine', '6-Mercaptopurine', '6-MP', 'Purinethol', 'Purixan (oral suspension formulation)', 

#328 
'Mesna', 'Anti Uron', 'Mesa', 'Mesnex', 'Mesnil', 'Mestian', 'Mistabron', 'Mistabronco', 'Mitexan', 'Mucolene', 'Neper', 'Novacarel', 'Siruta', 'Uromes', 'Uromitexan', 'Uroprot', 'Varimesna', 

#329 
'Methotrexate', 'amethopterin', 'MTX', 'Abitrexate', 'Alltrex', 'Antifolan', 'Artrait', 'Biometrox', 'Biotrexate', 'Caditrex', 'Cytotrexate', 'Ebetrexat', 'Emthexat', 'Emthexate', 'Ervemin', 'Farmitrexat', 'Fauldmetro', 'Folex PFS', 'Folitrax', 'Hextrate', 'Ifamet', 'Imutrex', 'Jylamvo', 'Ledertrexate', 'Ledertrexato', 'Lumexon', 'Matrex', 'Maxtrex', 'Medsatrexate', 'Merex', 'Metex', 'Methobax', 'Methoblastin', 'Methorex', 'Methotrexaat', 'Methotrexat', 'Methotrexato', 'Methotrexatum', 'Meticil', 'Metolate', 'Metotressato', 'Metotrexate', 'Metotrexato', 'Metotrexol', 'Metrex', 'Metrexan', 'Metrexato', 'Metrotex', 'Mexate', 'Miantrex CS', 'Neometho', 'Neotrexate', 'Nordimet', 'Novatrex', 'O Trexat', 'Oncotrex', 'Pharmatrexate', 'Remtrex', 'Reumatrex', 'Rextop', 'Rheumatrex', 'Tecnomet', 'Texate', 'Texorate', 'Tratoben', 'Tremetex', 'Trexall', 'Trexan', 'Trexeron', 'Trixilem', 'Unitrexate', 'Zexate', 

#330 
'Methoxsalen', '8-MOP', 'methoxypsoralen', 'Ammoidin', 'Deltasoralen', 'Dermox', 'Geralen', 'Geroxalen', 'Meladinina', 'Meladinine', 'Metoxaleno', 'Mopsoralen', 'Oxsoralen', 'Oxsoralen-Ultra', 'Puvasoralen', 'Ultramop', 'Uvadex', 'Xanthotoxin', 

#331 
'Methylprednisolone', 'methylprednisolone acetate', 'methylprednisolone sodium succinate', 'Adlone', 'Advantan', 'Adventan', 'Alergolon', 'Amethapred', 'Asmacortone', 'Avancort', 'Belon', 'Cortesa', 'Cortisolona', 'Decacort', 'Depmedalone', 'Depo Melcort', 'Depo Moderin', 'Depo-Medrate', 'Depo-Medrol', 'Depoject', 'Depomedrone', 'Deposet', 'Dispred', 'Duralone', 'Epizolone', 'Excelin', 'Hexilon', 'Indrol', 'Intidrol', 'Ivepred', 'Lameson', 'Lemod', 'Lesol', 'Lexcomet', 'Lexxema', 'M-Prednihexal', 'Medason', 'Medirona', 'Medisolu', 'Medixon', 'Medlin', 'Medlone', 'Mednin', 'Medralone', 'Medrate', 'Medrol', 'Medrone', 'Melon', 'Melone', 'Menisolon', 'Menisone', 'Mepredron', 'Meprolone Unipak', 'Meproson', 'Mepsolone', 'Mepson', 'Mesolone', 'Mesurin', 'Methapred', 'Methisol', 'Methybon', 'Methylon', 'Methylone', 'Methylprednis', 'Methylprednisolon', 'Methylprednisolonum', 'Methyran', 'Meticort', 'Metidrol', 'Metilbetasone', 'Metilprednisolona', 'Metilprednizolon-H', 'Metipred', 'Metisone', 'Metycortin', 'Metypred', 'Metypresol', 'Metysolon', 'NEO-Drol', 'Nirypan', 'Phadilon', 'Predisol', 'Predmetil', 'Predni M', 'Predni-M-Tablinen', 'Prednilem', 'Prednol', 'Prednol L', 'Prednovare', 'Prednox', 'Pretilon', 'Pridol', 'Promedrol', 'Radilem', 'Rumaxoi', 'Salon H9C', 'Sanexon', 'SOL-Melcort', 'Solocort-ACT', 'Solomet', 'Solu Moderin', 'Solumedrol', 'Somelon', 'Somerol', 'Stenirol', 'Succimed', 'Supresol', 'Thimelon', 'Tropidrol', 'Unimedrol', 'Urbason', 'Vanderm', 'Yumerole', 

#333 
'Midostaurin', 'PKC412', 'Rydapt', 'Tauritmo', 

#334 
'Mitomycin', 'mitomycin-C', 'MTC', 'Lyomit', 'Mitocin', 'Mitocyte', 'Mitosol', 'Mitozytrex', 'Mutamycin', 

#335 
'Mitotane', "o,p'-DDD", 'Lysodren', 

#336 
'Mitoxantrone', 'mitozantrone', 'Nitrol', 'Novantron', 'Novantrone', 

#338 
'Mogamulizumab', 'mogamulizumab-kpkc', 'KW-0761', 'Poteligeo', 

#341 
'Motesanib', 'AMG 706', 

#342 
'Moxetumomab pasudotox', 'moxetumomab pasudotox-tdfk', 'CAT-8015', 'HA22', 'Lumoxiti', 

#346 
'Nadroparin', 'Fraxiparine', 'Fraxodi', 

#347 
'Necitumumab', 'IMC-11F8', 'Portrazza', 

#348 
'Nedaplatin', 'nedaplat', '254-S', 'Aqupla', 'Jiebaishu', 

#349 
'Nelarabine', '506U78', 'Arranon', 'Atriance', 

#350 
'Neratinib', 'HKI-272', 'Nerlynx', 

#352 
'Nilotinib', 'AMN107', 'Tasigna', 

#353 
'Nilutamide', 'Anandron', 'Nilandron', 'Zandron', 

#354 
'Nimustine', 'ACNU', 'pimustine', 'Nidran', 

#355 
'Nintedanib', 'BIBF 1120', 'Cyendiv', 'Idofnib', 'Nifev', 'Nindanib', 'Nintena', 'Nintenib', 'Nintib', 'Ofev', 'Vargatef', 

#356 
'Niraparib', 'MK4827', 'Niranib', 'Zejula', 

#357 
'Nivolumab', 'BMS-936558', 'MDX-1106', 'ONO-4538', 'Opdivo', 

#359 
'Non-pegylated liposomal doxorubicin', 'liposome-encapsulated doxorubicin citrate', 'NPLD', 'Myocet', 

#360 
'Norethandrolone', 'Nilevar', 

#361 
'Obinutuzumab', 'afutuzumab', 'GA101', 'R7159', 'RO5072759', 'Gazyva', 'Gazyvaro', 

#362 
'Octreotide', 'octreotide acetate', 'octreotide immediate release', 'octreotide IR', 'SMS 201-995', 'Longastatina', 'Octrestatin', 'Octride', 'Okeron', 'Proclose', 'Samilstin', 'Sandostatin', 'Sandostatina', 'Sandostatine', 

#363 
'Octreotide LAR', 'octreotide acetate for injectable suspension', 'octreotide long-acting release', 'Longastatina LAR', 'Sandostatin LAR', 'Sandostatin LAR Depot', 'Sandostatina LAR', 'Sandostatine LAR', 

#364 
'Ofatumumab', 'HuMax-CD20', 'Arzerra', 'Kesimpta', 

#366 
'Olaparib', 'AZD-2281', 'AZD2281', 'KU-0059436', 'Lynparza', 'Olanib', 'Olaparix', 

#367 
'Olaratumab', 'IMC-3G3', 'LY3012207', 'Lartruvo', 

#368 
'Omacetaxine', 'HHT', 'homoharringtonine', 'omacetaxine mepesuccinate', 'Omapro', 'Synribo', 

#369 
'Omeprazole', 'Prilosec', 

#370 
'Onartuzumab', 'MetMAb', 'RO5490258', 

#375 
'Osimertinib', 'AZD9291', 'Osimert', 'Tagrisso', 'Tagrix', 

#377 
'Oxaliplatin', 'JM-83', 'RP-54780', 'SR-96669', 'Coxatin', 'Curaplat', 'Cure-X', 'Dacotin', 'Dacplat', 'Eloplat', 'Eloxatin', 'Eloxatine', 'Oplatin', 'OxaLitin', 'Oxiplat', 'Oxitan', 'Oxzucia', 'Sibatin', 'X-Plat', 'Xaloplat', 'Xylotin', 'Zildox', 

#378 
'Paclitaxel nanoparticle albumin-bound', 'ab-pac', 'ab-paclitaxel', 'albumin-bound paclitaxel', 'nab-paclitaxel', 'paclitaxel protein-bound', 'paclitaxel protein-bound particles for injectable suspension (albumin-bound)', 'ABI-007', 'Abraxane', 

#379 
'Paclitaxel', 'Abitaxel', 'Altaxel', 'Anzatax', 'Anzatec', 'Apealea', 'Asotax', 'Betaxel', 'Bristaxol', 'Britaxol', 'Clitaxel', 'Cytax', 'Daburex', 'Dalys', 'Drifen', 'Ebetaxel', 'Formoxol', 'Genetaxyl', 'Genexol', 'Gros', 'Ifaxol', 'Intaxel', 'Magytax', 'Medixel', 'Mitotax', 'Neotacs', 'Neotaxan', 'Neotaxl', 'Ofoxel', 'Oncotaxel', 'Onxol', 'Paclitax', 'Paclitaxin', 'Pacliteva', 'Pacxel', 'Padexol', 'Paklitaxfil', 'Panataxel', 'Parexel', 'Paxene', 'Paxenor', 'Paxus', 'Pazenir', 'Petaxel', 'Phyxol', 'Poltaxel', 'Praxel', 'Ribotax', 'Sindaxel', 'Taclipaxol', 'Tarvexol', 'Taxocris', 'Taxodiol', 'Taxol', 'Taxomedac', 'Taycovit', 'Unitaxel', 'Yewtaxan', 

#380 
'Pacritinib', 'SB1518', 'Vonjo', 

#381 
'Palbociclib', 'PD-0332991', 'Ibrance', 'Lucipalb', 'Palbace', 'Palbocap', 'Palbocent', 'Palbonix', 

#384 
'Panitumumab', 'ABX-EGF', 'clone E7.6.3', 'Vectibix', 

#385 
'Panobinostat', 'panobinostat lactate anhydrous', 'LBH589', 'Faridak', 'Farydak', 

#387 
'Pazopanib', 'GW786034B', 'Pazopater', 'Votrient', 

#388 
'Pegaspargase', 'peg-asparginase', 'PEG-L-asparaginase', 'pegasparaginase', 'Oncaspar', 

#391 
'Peginterferon alfa-2a', 'Pegasys', 

#392 
'Peginterferon alfa-2b', 'PEG-IFN alfa-2b', 'pegylated interferon alfa-2b', 'polyethylene glycol IFN-A2b', 'polyethylene glycol interferon alfa-2b', 'SCH 54031', 'PEG-Intron', 'PegIntron', 'Sylatron', 'ViraferonPeg', 

#393 
'Pegylated liposomal doxorubicin', 'doxorubicin HCl liposome injection', 'PLD', 'Caelyx', 'Celdoxome', 'Doxil', 'Doxosome', 'Doxulip', 'i-dox', 'Lipodox', 'Lippod', 'Natdox', 'Peg-Doxorub', 'Pegadria', 'Pegdoxine', 'Peglidox', 'Zolsketil', 

#394 
'Pembrolizumab', 'lambrolizumab', 'MK-3475', 'SCH 900475', 'Keytruda', 

#395 
'Pemetrexed', 'pemetrexed disodium', 'Alimta', 'Antifol', 'Armisarte', 'Ciambra', 'Kabipem', 'Pemcure', 'Pemetero', 'Pemetra', 'Pemetrex', 'Pemex', 'Pemfexy', 'Pemgem', 'Pemibenz', 'Pemnat', 'Pexotra', 

#397 
'Pentostatin', "2'-deoxycoformycin", 'dCF', 'Nipent', 

#400 
'Pertuzumab', '2C4', 'Rhumab 2C4', 'Omnitarg', 'Perjeta', 

#405 
'Pirarubicin', 'theprubicin', 'THP-doxorubicin', '1609-RB', 'Pinorubicin', 'Pinorubin', 'Therarubicin', 

#406 
'Pixantrone', 'pixantrone dimaleate', 'BBR 2778', 'Pixuvri', 

#408 
'Plicamycin', 'mithramycin', 'Mithracin', 

#410 
'Pomalidomide', '3-amino-thalidomide', 'CC-4047', 'CC4047', 'Actimid', 'Ibipolid', 'Imnovid', 'Pomalid', 'Pomalyst', 

#411 
'Ponatinib', 'ponatinib hydrochloride', 'AP24534', 'Iclusig', 

#414 
'Pralatrexate', 'Folotyn', 

#416 
'Pravastatin', 'Pravachol', 

#417 
'Prednisolone', 'delta(1)hydrocortisone', 'delta1-dehydro-hydrocortisone', 'deltahydrocortisone', 'metacortandralone', 'prednisolone acetate', 'prednisolone tebutate', 'Adnisolone', 'Aprednislon', 'Capsoid', 'Cortalone', 'Cortisolone', 'Cotolone', 'Dacortin H', 'Decaprednil', 'Decortin H', 'Delta-Cortef', 'Delta-Diona', 'Delta-Phoricol', 'Deltacortril', 'Deltasolone', 'Deltidrosol', 'Dhasolone', 'Di-Adreson-F', 'Dontisolon D', 'Estilsona', 'Fisopred', 'Frisolona', 'Gupisone', 'Hostacortin H', 'Hydeltra', 'Hydeltrasol', 'Klismacort', 'Kuhlprednon', 'Lenisolone', 'Lepi-Cortinolo', 'Linola-H N', 'Linola-H-Fett N', 'Longiprednil', 'Medicort', 'Meti-derm', 'Meticortelone', 'Millipred', 'Opredsone', 'Orapred', 'Panafcortelone', 'Precortisyl', 'Pred-Clysma', 'Predcor', 'Predeltilone', 'Predicort', 'Predni-Coelin', 'Predni-Helvacort', 'Prednicortelone', 'Prelone', 'Prenilone', 'Pri-Cortin', 'Veripred', 

#418 
'Prednisone', 'pred', 'Artinizona', 'Artrizona', 'Becortem', 'Bersen', 'Colisone', 'Cortancyl', 'Corticorten', 'Cortigen', 'Cortiol', 'Cortiprex', 'Cutason', 'Dacortin', 'Decortancyl', 'Decortin', 'Decortisyl', 'Dehydrocortison', 'Delcortin', 'Dellacorta', 'Delta Cortelan', 'Delta-Cortisone', 'Deltacortene', 'Deltacortone', 'Deltason', 'Deltasone', 'Deltisona', 'Dispersona', 'Drazone', 'Econosone', 'Ednaprom', 'Encorton', 'Erlanison', 'Flamacorten', 'Hostacortin', 'Ifison', 'Isolone', 'Lisacort', 'ME Korti', 'Meticorten', 'Nisocortec', 'Nisona', 'Nisone', 'Nizon', 'Nosipren', 'Novoprednisone', 'Orasone', 'Panafcort', 'Panasol-S', 'Pehacort', 'Pharmapred', 'Precortil', 'Predcort', 'Predeltin', 'Predicor', 'Predicorten', 'Predinis', 'Preditec', 'Prednax', 'Prednicap', 'Prednicen-M', 'Prednilonga-Retard', 'Predniment', 'Prednison', 'Prednisona', 'Prednisonum', 'Prednitone', 'Predson', 'Predsone', 'Predval', 'Procion', 'Prolix', 'Pronison', 'Pulmison', 'Rayos', 'Rectodelt', 'Senterlic', 'Sone', 'Steerometz', 'Sterapred', 'Trolic', 'Ultracorten', 'Vitazon', 'Winpred', 

#419 
'Procarbazine', 'ibenzmethyzin hydrochloride', 'ibenzmethyzine hydrochloride', 'procarbazine hydrochloride', 'NCI-C01810', 'Ro 4-6467/1', 'Indicarb', 'Matulane', 'Natulan', 'Natulanar', 'P-Carbazine', 'P-Carzine', 

#424 
'Quinine', 'Qualaquin', 

#426 
'Quizartinib', 'AC220', 'ASP2689', 'Vanflyta', 

#429 
'Radotinib', 'IY5511HCl', 'Supect', 

#431 
'Raltitrexed', 'raltitrexed disodium', 'TDX', 'ZD 1694', 'Tomudex', 

#433 
'Ramucirumab', 'IMC-1121B', 'LY3009806', 'Cyramza', 

#434 
'Ranimustine', 'MCNU', 'ranomustine', 'Cymer', 'Cymerin', 

#438 
'Regorafenib', 'BAY 73-4506', 'Nublexa', 'Regonix', 'Renib', 'Resihance', 'Stivarga', 

#441 
'Ribociclib', 'LEE-011', 'LEE011', 'Kisqali', 'Kryxana', 

#446 
'Rituximab', 'BI 695500', 'IDEC-102', 'IDEC-C2B8', 'PF-05280586', 'RTXM83', 'Ikgdar', 'Mabtas', 'MabThera', 'Reditux', 'Ristova', 'Rituxan', 'Rituxim', 'Transera-Kit', 

#447 
'Rituximab and hyaluronidase human', 'Rituxan Hycela', 

#451 
'Romidepsin', 'depsipeptide', 'FK228', 'FR901228', 'NSC 630176', 'Istodax', 

#453 
'Ropeginterferon alfa-2b', 'AOP2014', 'Besremi', 

#454 
'Rucaparib', 'AG-014699', 'CO-338', 'PF-0136738', 'Rubraca', 

#455 
'Ruxolitinib', 'ruxolitinib phosphate', 'INCB018424', 'Jakafi', 'Jakavi', 

#456 
'Sacituzumab govitecan', 'sacituzumab govitecan-hziy', 'IMMU-132', 'RS7-SN38', 'Trodelvy', 

#459 
'Sargramostim', 'GM-CSF', 'GMCSF', 'granulocyte macrophage colony stimulating factor', 'Leukine', 

#461 
'Selinexor', 'KPT-330', 'Nexpovio', 'Xpovio', 

#462 
'Selumetinib', 'AZD6244', 'Koselugo', 

#464 
'Semustine', 'MeCCNU', 'methyl-CCNU', 'methyl-lomustine', 'Semustina', 

#467 
'Sipuleucel-T', 'APC8015', 'Provenge', 

#469 
'Sonidegib', 'erismodegib', 'LDE225', 'Odomzo', 

#470 
'Sorafenib', 'BAY 43-9006', 'BAY 54-9085', 'Nexavar', 'Sorafenat', 'Soranib', 

#472 
'Streptozocin', 'STZ', 'Zanosar', 

#473 
'Sunitinib', 'sunitinib malate', 'SU011248', 'SU11248', 'Kitent', 'Lucisun', 'Suninat', 'Sunitix', 'Sutent', 

#475 
'Tagraxofusp', 'tagraxofusp-erzs', 'SL-401', 'Elzonris', 

#476 
'Talazoparib', 'BMN-673', 'Talzenna', 

#477 
'Talimogene laherparepvec', 'T-VEC', 'Imlygic', 'OncoVEX^GM-CSF', 

#478 
'Tamibarotene', 'Amnoid', 'Amnolake', 

#479 
'Tamoxifen', 'TAM', 'tamoxifen citrate', 'TMX', 'ICI-46474', 'Istubal', 'Nolvadex', 'Soltamox', 'Valodex', 

#481 
'Tegafur gimeracil oteracil', 'S-1', 'Teysuno', 'TS-One', 

#482 
'Tegafur and uracil', 'tegafur-uracil', 'Ftorafur', 'Luporal', 'Tefudex', 'Uftoral', 'Ufur', 'Uracel', 

#484 
'Temozolomide', 'TMZ', 'Gliotem', 'Temcad', 'Temizole', 'Temodal', 'Temodar', 'Temomedac', 'Temonat', 'Temoside', 'Temoz', 'Temzol', 

#485 
'Temsirolimus', 'CCI-779', 'Torisel', 

#486 
'Teniposide', 'VM-26', 'Vumon', 

#488 
'Thalidomide', 'Contergan', 'Distaval', 'Kevadon', 'Neurosedyn', 'Pantosediv', 'Sedalis', 'Sedoval K17', 'Softenon', 'Synovir', 'Talimol', 'Thaangio', 'Thalide', 'Thalido', 'Thalimide', 'Thalitero', 'Thalix', 'Thaloma', 'Thalomid', 'Zuvimide', 

#489 
'Thioguanine', '2-Amino-6-Mercaptopurine', '6-TG', '6-thioguanine', 'tioguanine', 'Lanvis', 'Tabloid', 'Thioxlant', 

#490 
'Thiotepa', 'TESPA', 'Thiophosphoamide', 'TSPA', 'Tepadina', 'Thioplex', 

#498 
'Tisagenlecleucel', 'tisagenlecleucel-T', 'CART19', 'CTL019', 'Kymriah', 

#499 
'Tivantinib', 'ARQ 197', 

#500 
'Tivozanib', 'AV-951', 'Fotivda', 

#503 
'Topotecan', 'SKF S-104864-A', 'Evotopin', 'Hycamtin', 'Potactasol', 'Topecan', 'Topotec', 

#504 
'Toremifene', 'Acapodene', 'Fareston', 'Farestone', 

#506 
'Tositumomab and I-131', 'tositumomab and I 131 tositumomab', 'tositumomab and iodine-131 tositumomab', 'Bexxar', 

#507 
'Trabectedin', 'ET-743', 'Yondelis', 

#508 
'Trametinib', 'trametinib dimethyl sulfoxide', 'GSK-1120212', 'GSK1120212', 'JTP-74057', 'Mekinist', 'Meqsel', 

#509 
'Tranexamic acid', 'Amixam', 'Cyklokapron', 'Hemostan', 'Prexam', 'Temsy', 'Tranofast', 

#512 
'Trastuzumab', 'Biceltis', 'CANMab', 'Herceptin', 'Herclon', 'Hertraz', 

#513 
'Trebananib', 'AMG 386', 

#514 
'Tremelimumab', 'ticilimumab', 'CP-675', 'CP-675206', 'Imjudo', 

#515 
'Treosulfan', 'Ovastat', 'Trecondi', 

#516 
'Trifluridine and tipiracil', 'trifluridine and tipiracil', 'trifluridine/tipiracil', 'TAS-102', 'Lonsurf', 

#518 
'Triptorelin', 'triptorelin pamoate', 'AY25650', 'CL118532', 'Decapeptyl', 'Detryptoreline', 'Diphereline', 'Gonapeptyl', 'Trelstar LA', 'Variopeptyl', 

#520 
'Ublituximab', 'LFB-R603', 'TG-1101', 'TG-20', 'TGTX-1101', 

#522 
'Uracil mustard', 'uramustine', 

#527 
'Valproate', 'valproic acid', 'Depacon', 'Depakine', 'Depakote', 'Encorate', 'Epibest', 'Epilim', 'Epival', 'Leeporate', 'Vallona', 'Valric', 

#528 
'Valrubicin', 'AD 32', 'Valstar', 'Valtaxin', 

#529 
'Vandetanib', 'AZD6474', 'ZD6474', 'Caprelsa', 'Lucivand', 'Zactima', 

#531 
'Veliparib', 'ABT-888', 

#533 
'Vemurafenib', 'PLX4032', 'RG7204', 'RO5185426', 'Zelboraf', 

#534 
'Venetoclax', 'ABT-199', 'GDC-0199', 'Venclexta', 'Venclyxto', 

#535 
'Vinblastine', 'chlorhexamide', 'vinblastine sulfate', 'vinblastine sulphate', 'vincaleukoblastine', 'VLB', 'Alkaban-AQ', 'Blastovin', 'Cellblastin', 'Cytoblastine', 'Erbablas', 'Exal', 'Faulblastina', 'Lemblastine', 'Periblastine', 'Rabinefil', 'Velban', 'Velbastine', 'Velbe', 'Vinblasin', 'Vinblastin', 'Vinblastina', 

#536 
'Vincristine', 'LCR', 'leurocristine', 'VCR', 'vincristine sulfate', 'Alcrist', 'Biocrist', 'Biocrystin', 'Cellcristin', 'Citomid', 'Crivosin', 'Farmistin CS', 'Fauldvincri', 'Krebin', 'Kyocristine', 'Nevexitin', 'Oncovin', 'Onkocristin', 'Pericristine', 'Pharmacristine', 'Tecnocris', 'Vincasar', 'Vinces', 'Vincosid', 'Vincran', 'Vincrex', 'Vincrifil', 'Vincrin', 'Vincrisin', 'Vincrisol', 'Vincristin', 'Vincristina', 'Vincristinesulfaat', 'Vincristinsulfat', 'Vincristinum', 'Vincrisul', 'Vinracin', 'Vinracine', 'Vinstin', 'Vintec', 

#537 
'Vincristine liposomal', 'vincristine sulfate liposome injection', 'VSLI', 'Marqibo', 

#538 
'Vindesine', 'DAVA', 'desacetylvinblastine amide', 'DVA', 'VDS', 'LY-099094', 'Eldesine', 'Eldisin', 'Eldisine', 'Enison', 'Fildesin', 'Gesidine', 

#539 
'Vinflunine', 'Javlor', 

#540 
'Vinorelbine', 'NVB', 'vinorelbine tartrate', 'KW-2307', 'Binorel', 'Biovelbin', 'Eunades', 'Flonorbin', 'Navelbine', 'Neoben', 'Relbovin', 'Vinelbine', 'Vinorelbel', 'Vinotec', 

#541 
'Vismodegib', 'GDC-0449', 'Erivedge', 

#545 
'Vorinostat', 'Zolinza', 

#546 
'Vosaroxin', 'voreloxin', 'SNS-595', 

#548 
'Zidovudine', 'azidothymidine', 'AZT', 'ZDV', 'Aztec', 'Retrovir', 

#549 
'Ziv-aflibercept', 'aflibercept', 'VEGF trap', 'Zaltrap', 

#1608 
'External beam radiotherapy', 

#3231 
'Capmatinib', 'capmatinib', 'INC280', 'Tabrecta', 

#3563 
'Enfortumab vedotin', 'enfortumab vedotin-ejfv', 'ASG-22CE', 'Padcev', 

#3590 
'Trastuzumab deruxtecan', 'fam-trastuzumab deruxtecan-nxki', 'DS-8201a', 'Enhertu', 

#3652 
'Abarelix', 'Plenaxis', 

#4380 
'Belantamab mafodotin', 'belantamab mafodotin-blmf', 'GSK2857916', 'Blenrep', 

#4683 
'Tucatinib', 'irbinitinib', 'ARRY-380', 'ONT-380', 'Tukysa', 

#4940 
'Daratumumab and hyaluronidase', 'daratumumab and hyaluronidase-fihj', 'Darzalex Faspro', 

#6008 
'Alitretinoin', 'ALRT1057', 'LGD1057', 'Panretin', 'Panretyn', 'Panrexin', 

#6632 
'Brexucabtagene autoleucel', 'KTE-X19', 'Tecartus', 

#10396 
'Alpelisib', 'BYL719', 'Piqray', 

#10767 
'Amonafide', 'Quinamed', 'Xanafide', 

#11533 
'Amoxicillin', 'Amoxi', 'Amoxihexal', 'Amoxil', 'Biomox', 

#12017 
'Ampicillin', 

#12637 
'Aumolertinib', 'almonertinib', 'HS-10296', 'Amelie', 

#13351 
'Pemigatinib', 'INCB054828', 'Pemazyre', 

#13651 
'Ripretinib', 'DCC-2618', 'Qinlock', 

#13759 
'Selpercatinib', 'LOXO-292', 'Retevmo', 'Retsevmo', 

#14235 
'Decitabine and cedazuridine', 'ASTX727', 'Inqovi', 

#14322 
'Bismuth subcitrate', 

#14330 
'Bismuth subsalicylate', 'Pepto-Bismol', 

#14742 
'Camrelizumab', 'HR-301210', 'SHR-1210', 'AiRuiKa', 

#18352 
'Relugolix', 'TAK-385', 'Orgovyx', 'Relumina', 

#18359 
'Elacestrant', 'RAD1901', 'Orserdu', 

#18741 
'Envafolimab', 'KN 035', 

#18846 
'Trimetrexate', 'trimetrexate glucuronate', 'Neutrexin', 

#19782 
'Tepotinib', 'EMD-1214063', 'MSC-2156119', 'MSC-2156119J', 'Tepmetko', 

#20248 
'Futibatinib', 'TAS-120', 'Lytgobi', 

#20851 
'NovoTTF-100A system (Optune)', 'PMA P100034/S013', 'Optune', 

#21215 
'Lisocabtagene maraleucel', 'JCAR017', 'Breyanzi', 'Liso-cel', 

#23426 
'Idecabtagene vicleucel', 'ide-cel', 'bb2121', 'Abecma', 

#25334 
'Avapritinib', 'BLU-285', 'Ayvakit', 'Ayvakyt', 

#25485 
'Pexidartinib', 'PLX3397', 'Turalio', 

#25527 
'Pralsetinib', 'BLU-667', 'Gavreto', 

#25815 
'Stilbamidine', 'stilbamidine isetionate', 

#26763 
'Lurbinectedin', 'PM-01183', 'Zepzelca', 

#26852 
'Metronidazole', 'Flagyl', 

#26950 
'Naxitamab', 'naxitamab-gqgk', 'Danyelza', 

#27930 
'Tetracycline', 'Panmycin', 'Sumycin', 'Tetracyn', 

#27982 
'Tripotassium dicitratobismuthate', 'De-Noltab', 

#29688 
'Belzutifan', 'MK6482', 'PT2977', 'Welireg', 

#29753 
'Amivantamab', 'amivantamab-vmjw', 'JNJ-61186372', 'Rybrevant', 

#29973 
'Azacitidine oral', 'CC-486', 'Onureg', 

#32384 
'Penpulimab', 'AK105', 

#32625 
'Adavosertib', 'AZD-1775', 'MK-1775', 

#34403 
'Colchicine', 'Colcrys', 'Mitigare', 

#34976 
'Dostarlimab', 'dostarlimab-gxly', 'TSR-042', 'Jemperli', 

#35064 
'Serplulimab', 'HLX10', 'Hansizhuang', 

#36080 
'Sugemalimab', 'Cejemly', 

#38881 
'Allogeneic stem cells', 

#43485 
'Sirolimus protein-bound particles', 'nab-rapamycin', 'nab-sirolimus', 'ABI-009', 'Fyarro', 

#45472 
'Suramin', 'Antrypol', 

#45753 
'Adagrasib', 'MRTX849', 'Krazati', 

#47700 
'Tebentafusp', 'tebentafusp-tebn', 'IMCgp100', 'Kimmtrak', 

#48561 
'Fedratinib', 'SAR302503', 'TG101348', 'Inrebic', 

#48632 
'Zimberelimab', 'AB122', 'GLS-010', 

#49082 
'Trastuzumab and hyaluronidase', 'trastuzumab and hyaluronidase-oysk', 'Herceptin Hylecta', 

#50482 
'Zanubrutinib', 'BGB-3111', 'Brukinsa', 

#51224 
'Furmonertinib', 'alflutinib', 'alflutinib mesylate', 'furmonertinib mesylate', 'ASK120067', 'AST2818', 'Ivesa', 

#51229 
'Ciltacabtagene autoleucel', 'cilta-cel', 'JNJ-68284528', 'LCAR-B38M', 'Carvykti', 

#53780 
'Asciminib', 'ABL001', 'Scemblix', 

#53908 
'Loncastuximab tesirine', 'loncastuximab tesirine-lpyl', 'ADCT-402', 'Zynlonta', 

#54224 
'Tazemetostat', 'E7438', 'EPZ6438', 'Tazverik', 

#59120 
'Nivolumab and relatlimab', 'nivolumab and relatlimab-rmbw', 'BMS-986016', 'Opdualag', 

#59220 
'Interferon alfa-2c', 'Berofor', 

#59221 
'Interferon alfa-n1', 'Wellferon', 

#59291 
'Margetuximab', 'MGAH22', 'Margenza', 

#59461 
'Sotorasib', 'AMG 510', 'Lumakras', 'Lumykras', 

#59505 
'Umbralisib', 'TGR-1202', 'Ukoniq', 

#61131 
'Sintilimab', 'IBI 308', 'Tyvyt', 

#61306 
'Melphalan flufenamide', 'melflufen', 'J1', 

#61419 
'Pirtobrutinib', 'LOXO-305', 'Jaypirca', 

#64463 
'Tislelizumab', 'BGB-A317', 

#64471 
'Toripalimab', 'JS001', 'TAB001', 'Tuoyi', 

#65150 
'Teclistamab', 'teclistamab', 'teclistamab-cqyv', 'JNJ 64007957', 'Tecvayli', 

#69109 
'Mobocertinib', 'AP-32788', 'TAK-788', 'Exkivity', 

#71307 
'Tisotumab vedotin', 'tisotumab vedotin-tftv', 'HuMax-TF-ADC', 'Tivdak', 

#75279 
'Lanreotide LAR', 'lanreotide long-acting release', 'Somatuline Depot', 

#75337 
'Pimitespib', 'TAS-116', 'Jeselhy', 

#76031 
'Prednimustine', 'Mostarina', 'Sterocyt', 

#76563 
'Pipobroman', 'Vercite', 'Vercyte', 

#93818 
'Polatuzumab vedotin', 'polatuzumab vedotin-piiq', 'DCDS4501A', 'Polivy', 

#109643 
'Mirvetuximab soravtansine', 'mirvetuximab soravtansine-gynx', 'IMGN853', 'Elahere', 

#110427 
'Agatolimod', 

#110498 
'BMS-275291', 

#110733 
'Farletuzumab', 

#110743 
'Figitumumab', 

#111261 
'Mosunetuzumab', 'mosunetuzumab-axgb', 'BTCT4465A', 'RG7828', 'Lunsumio', 

#111273 
'Nadofaragene firadenovec', 'nadofaragene firadenovec-vncg', 'SCH 721015', 'Adstiladrin', 'Instiladrin', 

#111358 
'Olutasidenib', 'FT-2102', 'Rezlidhia', 

#111427 
'Pyrotinib', 'Irene', 

#111602 
'Tirapazamine', 

#111630 
'Vadimezan', 

#114346 
'Buserelin', 'HOE 766', 'ICI 123215', 'S74-6766', 'Bigonist', 'Etilamide', 'Profact', 'Receptal', 'Suprecur', 'Suprefact', 

#114432 
'Lifileuecel', 'LN-144', 'Contego', 

#114494 
'Tabelecleucel', 'EBV-CTLs', 'ATA129', 'Ebvallo', 'Tab-cel', 

#114706 
'CART-EGFRvIII', 
]]
