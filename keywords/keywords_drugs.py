drug_keywords = [word.lower() for word in [
    #ibuprofen
    'Ibuprofen', 'IBUPROFEN', 'ibuprofen', 

    #acetaminophen
    'Acetaminophen', 'ACETAMINOPHEN', 'acetaminophen', 

    #lidocaine
    'lidocaine', 'LIDOCAINE', 'Lidocaine', 

    #esomeprazole
    'Esomeprazole', 'esomeprazole', 'ESOMEPRAZOLE', 

    #pregabalin
    'PREGABALIN', 'pregabalin', 'Pregabalin', 

    #oxycodone
    'OXYCODONE', 'oxycodone', 'Oxycodone', 

    #fluticasone propionate
    'fluticasone propionate', 'FLUTICASONE PROPIONATE', 'Fluticasone Propionate', 'Fluticasone propionate', 

    #valsartan
    'VALSARTAN', 'Valsartan', 'valsartan', 

    #doxycycline
    'DOXYCYCLINE', 'Doxycycline', 'doxycycline', 

    #eszopiclone
    'Eszopiclone', 'eszopiclone', 'ESZOPICLONE', 

    #sildenafil
    'sildenafil', 'SILDENAFIL', 'Sildenafil', 

    #abiraterone
    'abiraterone', 'ABIRATERONE', 'Abiraterone', 

    #tadalafil
    'tadalafil', 'TADALAFIL', 'Tadalafil', 

    #aspirin
    'ASPIRIN', 'aspirin', 'Aspirin', 

    #aripiprazole
    'Aripiprazole', 'ARIPIPRAZOLE', 'aripiprazole', 

    #budesonide
    'BUDESONIDE', 'Budesonide', 'budesonide', 

    #pradaxa
    'Pradaxa', 

    #celecoxib
    'Celecoxib', 'celecoxib', 'CELECOXIB', 

    #ezetimibe
    'EZETIMIBE', 'ezetimibe', 'Ezetimibe', 

    #vytorin
    'VYTORIN', 

    #nicotine
    'nicotine', 'Nicotine', 'NICOTINE', 

    #duloxetine
    'Duloxetine', 'duloxetine', 'DULOXETINE', 

    #benicar
    'Benicar', 

    #methylphenidate
    'methylphenidate', 'METHYLPHENIDATE', 'Methylphenidate', 

    #insulin lispro
    'Insulin lispro', 'insulin lispro', 'Insulin Lispro', 

    #adalimumab
    'Adalimumab', 'adalimumab', 

    #paracetamol
    'Paracetamol', 'PARACETAMOL', 

    #liraglutide
    'liraglutide', 'LIRAGLUTIDE', 'Liraglutide', 

    #pemetrexed
    'Pemetrexed', 'pemetrexed', 'PEMETREXED', 

    #fenofibrate
    'fenofibrate', 'Fenofibrate', 'FENOFIBRATE', 

    #rivaroxaban
    'Rivaroxaban', 'RIVAROXABAN', 'rivaroxaban', 

    #everolimus
    'Everolimus', 'EVEROLIMUS', 'everolimus', 

    #capecitabine
    'capecitabine', 'CAPECITABINE', 'Capecitabine', 

    #darunavir
    'Darunavir', 'DARUNAVIR', 'darunavir', 

    #triamcinolone
    'Triamcinolone', 'TRIAMCINOLONE', 

    #buprenorphine
    'Buprenorphine', 'buprenorphine', 'BUPRENORPHINE', 

    #divalproex sodium
    'Divalproex sodium', 'Divalproex Sodium', 'divalproex sodium', 'DIVALPROEX SODIUM', 

    #ranibizumab
    'Ranibizumab', 'RANIBIZUMAB', 'ranibizumab', 

    #castor oil
    'Castor Oil', 'CASTOR Oil', 'Castor oil', 

    #melatonin
    'Melatonin', 

    #epoetin alfa
    'epoetin alfa', 

    #fentanyl
    'Fentanyl', 'FENTANYL', 

    #hydrocodone bitartrate
    'hydrocodone bitartrate', 'HYDROCODONE BITARTRATE', 'Hydrocodone Bitartrate', 

    #ustekinumab
    'ustekinumab', 'Ustekinumab', 

    #lyrica
    'Lyrica', 

    #rituximab
    'rituximab', 'Rituximab', 

    #filgrastim
    'Filgrastim', 

    #diovan
    'Diovan', 

    #lantus
    'Lantus', 

    #insulin glargine
    'Insulin Glargine', 'insulin glargine', 'Insulin glargine', 

    #quetiapine
    'Quetiapine', 'quetiapine', 'QUETIAPINE', 

    #tamiflu
    'Tamiflu', 

    #xeloda
    'Xeloda', 

    #isentress
    'ISENTRESS', 

    #raltegravir
    'Raltegravir', 'RALTEGRAVIR', 

    #janumet
    'JANUMET', 

    #cinacalcet
    'Cinacalcet', 'CINACALCET', 

    #atazanavir
    'Atazanavir', 'ATAZANAVIR', 

    #hydrocortisone cream
    'Hydrocortisone Cream', 

    #novolog
    'NOVOLOG', 

    #insulin aspart
    'Insulin Aspart', 'insulin aspart', 

    #warfarin
    'Warfarin', 

    #rosuvastatin
    'ROSUVASTATIN', 'Rosuvastatin', 

    #lantus solostar
    'LANTUS SOLOSTAR', 'Lantus Solostar', 

    #humira
    'Humira', 

    #januvia
    'JANUVIA', 

    #sitagliptin
    'sitagliptin', 'Sitagliptin', 

    #xolair
    'XOLAIR', 'Xolair', 

    #omalizumab
    'omalizumab', 

    #xarelto
    'XARELTO', 'Xarelto', 

    #vaccines
    'Vaccines', 

    #imatinib
    'imatinib', 'Imatinib', 'IMATINIB', 

    #evista
    'Evista', 

    #adderall xr
    'Adderall XR', 

    #memantine
    'MEMANTINE', 'Memantine', 'memantine', 

    #aranesp
    'ARANESP', 

    #darbepoetin alfa
    'darbepoetin alfa', 

    #sensipar
    'Sensipar', 

    #xgeva
    'XGEVA', 

    #denosumab
    'denosumab', 

    #stelara
    'STELARA', 'Stelara', 

    #oxycontin
    'OxyContin', 

    #abilify
    'ABILIFY', 

    #vyvanse
    'Vyvanse', 

    #prezista
    'PREZISTA', 

    #raloxifene
    'Raloxifene', 

    #seroquel xr
    'SEROQUEL XR', 

    #lisdexamfetamine
    'Lisdexamfetamine', 'lisdexamfetamine', 

    #copaxone
    'Copaxone', 

    #dexlansoprazole
    'dexlansoprazole', 'DEXLANSOPRAZOLE', 'Dexlansoprazole', 

    #metoprolol
    'METOPROLOL', 'Metoprolol', 

    #trastuzumab
    'trastuzumab', 'TRASTUZUMAB', 'Trastuzumab', 

    #palivizumab
    'palivizumab', 

    #infliximab
    'infliximab', 'Infliximab', 'INFLIXIMAB', 

    #abatacept
    'Abatacept', 'abatacept', 

    #gravol
    'Gravol', 

    #reyataz
    'REYATAZ', 

    #pepto bismol
    'Pepto Bismol', 

    #levemir
    'LEVEMIR', 'Levemir', 

    #insulin detemir
    'insulin detemir', 'Insulin Detemir', 

    #tiotropium bromide
    'Tiotropium Bromide', 'TIOTROPIUM BROMIDE', 

    #lucentis
    'LUCENTIS', 

    #tylenol pm
    'Tylenol PM', 

    #enbrel
    'ENBREL', 

    #etanercept
    'etanercept', 

    #renvela
    'Renvela', 

    #oseltamivir
    'Oseltamivir', 'OSELTAMIVIR', 

    #crestor
    'CRESTOR', 'Crestor', 

    #aciphex
    'AcipHex', 'Aciphex', 

    #ventolin hfa
    'VENTOLIN HFA', 

    #lunesta
    'Lunesta', 

    #celebrex
    'CELEBREX', 

    #solifenacin
    'Solifenacin', 

    #mometasone
    'Mometasone', 

    #benadryl
    'Benadryl', 

    #nexplanon
    'Nexplanon', 

    #viagra
    'Viagra', 

    #synthroid
    'Synthroid', 

    #prevnar 13
    'PREVNAR 13', 

    #pitocin
    'Pitocin', 

    #rebif
    'Rebif', 'REBIF', 

    #nexium
    'NEXIUM', 

    #cymbalta
    'Cymbalta', 

    #flovent hfa
    'FLOVENT HFA', 

    #humalog
    'Humalog', 

    #dexilant
    'Dexilant', 

    #epogen
    'EPOGEN', 

    #adderall
    'Adderall', 

    #remicade
    'REMICADE', 

    #cialis
    'Cialis', 

    #proair hfa
    'PROAIR HFA', 

    #avonex
    'AVONEX', 'Avonex', 

    #fingolimod
    'fingolimod', 'FINGOLIMOD', 'Fingolimod', 

    #synagis
    'Synagis', 

    #alimta
    'Alimta', 

    #humalog kwikpen
    'Humalog KwikPen', 

    #namenda
    'Namenda', 

    #bevacizumab
    'bevacizumab', 'Bevacizumab', 

    #lipitor
    'Lipitor', 

    #heparin
    'HEPARIN', 'Heparin', 

    #afinitor
    'Afinitor', 

    #nasonex
    'Nasonex', 

    #victoza
    'Victoza', 

    #avonex pen
    'Avonex Pen', 

    #zetia
    'Zetia', 

    #dabigatran
    'Dabigatran', 

    #orencia
    'ORENCIA', 

    #suboxone
    'Suboxone', 

    #neupogen
    'NEUPOGEN', 

    #zytiga
    'Zytiga', 

    #telaprevir
    'Telaprevir', 

    #ritalin
    'Ritalin', 

    #gilenya
    'Gilenya', 

    #atripla
    'Atripla', 

    #symbicort
    'SYMBICORT', 

    #avastin
    'Avastin', 

    #truvada
    'Truvada', 

    #pegfilgrastim
    'pegfilgrastim', 

    #levothyroxine
    'Levothyroxine', 

    #herceptin
    'Herceptin', 

    #complera
    'COMPLERA', 

    #stribild
    'Stribild', 

    #rabeprazole
    'Rabeprazole', 

    #glatiramer
    'Glatiramer', 

    #neulasta
    'Neulasta', 

    #insulin
    'Insulin', 

    #lovaza
    'LOVAZA', 

    #atorvastatin
    'Atorvastatin', 

    #vesicare
    'VESIcare', 

    #restasis
    'RESTASIS', 

    #androgel
    'AndroGel', 'Androgel', 

]]
