PART NINE – HOW DOES PROBABILITY HELP MACHINES MAKE DECISIONS? UNDERSTANDING PROBABILITY AND PROBABILITY DISTRIBUTIONS

Ungalukku oru email varudhu-nu imagine pannunga.

Andha email-la, "Congratulations! You've won a free iPhone. Click here to claim your prize!"-nu message irukku.

Idhu genuine email-ah? Illa spam email-ah?

Neenga message-ah paathadhum, idhu spam-ah irukkum-nu suspect pannuveenga.

Aana oru Machine Learning model idha epdi decide pannum?

Adhu email-la irukkura words, sender details, links, previous spam patterns-nu pala information-ah analyse pannum.

Adhukku apram, indha email spam-ah irukka evvalavu chance irukku-nu oru probability estimate generate pannalaam.

For example, model indha email spam-ah irukka ninety percent probability irukku-nu estimate pannudhu-nu vechukkonga.

Appo andha email kandippa spam-nu arthama?

Illa.

Ninety percent probability-na, model-oda estimate padi spam-aaga irukkura chance adhigama irukku-nu artham. Aana adhu hundred percent guarantee illa. Model estimate-oda accuracy-um adhu train aana data and model quality-ah depend pannum.

Indha maadhiri uncertainty irukkura situations-la dhaan Probability romba useful-ah irukku.

Innaiku probability-na enna, adha epdi calculate panradhu, Conditional Probability epdi work aagudhu, Probability Distribution-na enna-nu step by step-ah understand pannalaam.

PROBABILITY – MEASURING THE CHANCE OF SOMETHING HAPPENING

First, namma everyday life-la nadakkura oru simple situation-ah eduthukalaam.

Neenga weather forecast paakureenga.

Adhula tomorrow rain vara seventy percent chance irukku-nu solludhu.

Idhoda meaning enna?

Tomorrow kandippa rain varum-nu artham illa.

Rain varradhukku irukkura possibility adhigama irukku-nu forecast indicate pannudhu.

Oru event nadakkuradhukku irukkura chance-ah numerical value moolama represent panradhu dhaan Probability.

Probability-ku values zero-lendhu one varaikkum irukkum.

Zero-na andha event nadakka chance illai.

One-na andha event kandippa nadakkum.

Idhai percentage-ah kooda represent pannalaam.

Zero point five-na fifty percent.

Zero point seven-na seventy percent.

One-na hundred percent.

So, probability value zero-lendhu one varaikkum irukkum.

Ippo indha values-ah konjam practical-ah understand pannalaam.

Oru coin-ah toss panreenga-nu vechukkonga.

Coin toss pannumbodhu rendu possible outcomes irukku.

Heads illa Tails.

Coin fair-ah irundhaa, Heads varradhukku fifty percent chance irukku. Tails varradhukkum fifty percent chance irukku.

Inga coin toss panradhu oru Experiment.

Heads illa Tails maadhiri kidaikkakoodiya result-ah Outcome-nu solluvom.

Indha experiment-la possible-ah kidaikkakoodiya ella outcomes-oda collection-ku Sample Space-nu peru.

Namma coin example-la Sample Space-na Heads and Tails.

Ippo Heads varradhukku probability calculate pannanumna, favourable outcomes count-ah total possible outcomes count-ala divide pannalaam.

Aana indha simple formula use panna, ella possible outcomes-um equally likely-ah irukkanum.

Namma fair coin example-la Heads and Tails rendu outcomes-um equally likely-ah irukku.

Inga Heads varradhukku oru favourable outcome irukku.

Total possible outcomes rendu.

So, one divided by two.

Result zero point five.

Adhaavathu fifty percent.

Idhudhaan Probability calculate panradhoda basic idea.

HOW DO WE CALCULATE PROBABILITY?

Innor u simple example-ah paakalaam.

Oru box-la ten balls irukku-nu imagine pannunga.

Adhula six red balls and four blue balls irukku.

Neenga paakkaama oru ball-ah edukkureenga.

Ippo red ball kidaikkuradhukku evvalavu probability irukku?

Total balls ten.

Red balls six.

So, red ball varradhukku probability six divided by ten.

Adhu zero point six.

Adhaavathu sixty percent.

Blue ball kidaikkuradhukku probability four divided by ten.

Adhu zero point four.

Adhaavathu forty percent.

Inga oru important observation irukku.

Red ball varradhukku chance adhigam. Aana blue ball varradhukkum chance irukku.

Probability adhigama irukkuradhu-na andha event kandippa nadakkum-nu artham illa.

Adhu nadakka irukkura chance comparatively adhigam-nu mattum dhaan artham.

Indha difference-ah purinjikkaradhu Machine Learning-la romba important.

WHY DOES MACHINE LEARNING NEED PROBABILITY?

Ippo namma spam email example-ku thirumbi varalaam.

Oru email vandhirukku.

Adhula suspicious words irukku. Unknown sender irukkaaru. Oru unusual link-um irukku.

Model indha information ellathayum analyse pannudhu.

Adhukku apram, indha email spam-ah irukka probability-ah estimate pannudhu.

Suppose model spam probability-ah zero point nine-nu estimate pannudhu.

Adhaavathu ninety percent.

Genuine email-ah irukka probability zero point one-nu irukkalaam.

Adhaavathu ten percent.

Inga rendu probability values-um total-ah one, adhaavathu hundred percent.

Ippo application oru decision edukkanum.

For example, spam probability fifty percent-ku mela irundhaa spam folder-ku move pannalaam-nu oru threshold set pannirukkalaam.

Threshold-na decision edukka use panra oru predefined limit.

Indha example-la spam probability zero point nine. Adhu threshold-ah vida adhigam.

So, email spam folder-ku move aagalaam.

Aana threshold-ah change panninaa decision-um change aagalaam.

For example, important business emails-ah thappa spam folder-ku anuppakoodaadhu-nu oru application strict-ah irukkalaam.

Appo spam-nu classify panradhukku higher threshold use pannalaam.

Idhula irundhu namakku oru vishayam puriyudhu.

Probability model-ku uncertainty-ah numerical-ah represent panna help pannudhu.

Threshold application-ku andha probability base panni decision edukka help pannudhu.

Aana indha probability values epdi calculate aagudhu-nguradhula innum oru important concept irukku.

Adhu dhaan Conditional Probability.

CONDITIONAL PROBABILITY – WHEN ONE THING DEPENDS ON ANOTHER

Oru college-la students-oda attendance and exam results-ah analyse panrom-nu imagine pannunga.

Students-la sila per regular-ah classes attend panraanga.

Sila per irregular-ah attend panraanga.

Ippo randomly oru student-ah select panninaa, avar exam pass panra probability enna-nu calculate panna mudiyum.

Aana attendance details-um namakku theriyudhu-nu vechukkonga.

Andha student regular-ah classes attend panraar-nu already theriyum.

Appo avar pass panra probability-ah calculate panna, overall student population-ah mattum consider panna thevai illa.

Regular-ah attend panra students group-ah mattum consider pannalaam.

Idhudhaan Conditional Probability-oda basic idea.

Conditional Probability-na oru condition pathina information already therinja situation-la, andha condition-oda basis-la innoru event nadakkuradhukku irukkura probability.

Idhu rendu events-um kandippa cause-and-effect relationship-la irukku-nu artham illa. Namakku kidaikkura additional information base panni probability-ah calculate panrom-nguradhu dhaan important.

Idhai simple-ah purinjikka, rendu events-ah identify pannalaam.

Event A-na student exam pass panradhu.

Event B-na student regular-ah classes attend panradhu.

Ippo namakku B nadandhirukku-nu theriyum.

Andha condition-la A nadakkuradhukku irukkura probability dhaan Conditional Probability.

Mathematically, idhai P of A given B-nu represent pannuvom.

Inga given B-na B nadandhirukku-ngura information namakku already theriyum-nu artham.

Oru simple numerical example paakalaam.

Oru college-la hundred students irukkaanga-nu vechukkonga.

Adhula sixty students regular-ah classes attend panraanga.

Indha sixty students-la forty-eight students exam pass panraanga.

Ippo regular-ah attend panra students-la oru student exam pass panradhukku probability enna?

Inga namma total hundred students-ah consider panna koodaadhu.

Yenna, namakku regular-ah attend panra students pathina information already theriyum.

So, total sixty students dhaan namma consider pannanum.

Andha sixty students-la forty-eight students pass pannirukkaanga.

So, probability forty-eight divided by sixty.

Result zero point eight.

Adhaavathu eighty percent.

Idhudhaan Conditional Probability.

Overall students-la pass panra probability calculate panradhu vera.

Regular-ah attend panra students-la pass panra probability calculate panradhu vera.

Condition change aagumbodhu probability-um change aagalaam.

Machine Learning-la indha concept romba useful.

For example, oru customer already oru product-ah purchase pannirukkaaru-nu therinjaa, avar related product-ah purchase panradhukku irukkura probability-ah calculate panna mudiyum.

Adhe maadhiri, email-la particular words irukkuradhu therinjaa, adhu spam-ah irukka probability-ah estimate panna mudiyum.

Oru event-oda probability-ah additional information base panni understand panradhukku Conditional Probability help pannudhu.

PROBABILITY DISTRIBUTION – HOW ARE DIFFERENT POSSIBLE VALUES DISTRIBUTED?

Ippo probability-ah calculate panradhu purinjikittom.

Aana namma kitta oru experiment irukku-nu vechukkonga.

Adhula different outcomes varalaam.

Ovvoru outcome-ukkum different probability irukkalaam.

Indha possible outcomes-um adhukku corresponding probabilities-um epdi organize pannappadudhu?

Adha purinjikka Probability Distribution use aagudhu.

Probability Distribution-na oru random variable edukkakoodiya possible values-um, ovvoru value-ukkum irukkura probability-um epdi distribute aagudhu-nguradha describe panra mathematical representation.

First, Random Variable-na enna-nu purinjikkalaam.

Oru random experiment-oda outcome-ah numerical value moolama represent panra variable dhaan Random Variable.

For example, oru coin-ah three times toss panrom-nu vechukkonga.

Namakku evvalavu Heads kidaikkudhu-nguradha X-nu represent pannalaam.

X-oda possible values zero, one, two, illa three.

Moonu toss-la oru Heads-um varaama irukkalaam.

Oru Heads varalaam.

Rendu Heads varalaam.

Moonu Heads kooda varalaam.

Indha ovvoru possible value-ukkum oru probability irukkum.

Andha values-um probabilities-um together-ah represent panradhu dhaan Probability Distribution.

DISCRETE AND CONTINUOUS PROBABILITY DISTRIBUTIONS

Probability Distribution-la rendu important types irukku.

Discrete Probability Distribution and Continuous Probability Distribution.

First, Discrete Probability Distribution-ah paakalaam.

Discrete-na count panna mudiyura separate values.

For example, oru family-la irukkura children count zero, one, two, three-nu irukkalaam.

Oru coin-ah three times toss pannumbodhu kidaikkura Heads count zero, one, two, three-nu irukkalaam.

Indha maadhiri count panna mudiyura values-ah represent panra probability distribution-ku Discrete Probability Distribution-nu peru.

Inga namma coin toss example-ah continue pannalaam.

Three times coin toss pannumbodhu possible-ah kidaikkura Heads count zero-lendhu three varaikkum irukkum.

Fair coin-na, zero Heads kidaikkuradhukku probability one by eight.

One Head kidaikkuradhukku probability three by eight.

Two Heads kidaikkuradhukku probability three by eight.

Three Heads kidaikkuradhukku probability one by eight.

Indha possible values and probabilities ellathayum together-ah represent panninaa, adhu oru Discrete Probability Distribution.

Inga oru important point.

Indha possible outcomes-oda probabilities ellathayum add panninaa, total one varanum.

Yenna, experiment mudinjadhukku apram zero, one, two, illa three Heads-la edhaavadhu oru outcome kandippa kidaikkum.

Ippo Continuous Probability Distribution-ah paakalaam.

Continuous-na oru range-kulla pala possible numerical values edukkakoodiya measurements.

For example, oru person's height.

Height one hundred and sixty centimetres, one hundred and sixty point five centimetres, one hundred and sixty point five five centimetres-nu different values-ah irukkalaam.

Adhe maadhiri temperature, weight and travel time maadhiri measurements-um continuous values-ah represent pannalaam.

Indha maadhiri continuous numerical values-oda probability distribution-ah Continuous Probability Distribution-nu solluvom.

Inga oru important difference irukku.

Discrete values-ah count panna mudiyum.

Continuous values oru range-kulla theoretically innumerable possible values-ah edukkalaam.

Continuous distribution-la probability-ah usually oru range of values-ku calculate pannuvom. Oru exact value mattum edukkura probability zero-ah irukkum.

Machine Learning-la indha rendu types of distributions-um different situations-la use aagum.

NORMAL DISTRIBUTION – THE FAMILIAR BELL-SHAPED CURVE

Continuous Probability Distribution-la romba famous-ah use aagura oru distribution dhaan Normal Distribution.

Idhai Bell Curve-nu kooda solluvanga.

Yenna, idhoda graph oru bell shape maadhiri irukkum.

Oru simple example-ah students-oda exam marks-ah eduthukonga.

Oru large group of students exam ezhudhiyirukkaanga-nu imagine pannunga.

Most students average marks-ku pakkathula score pannirukkaanga.

Romba kammi marks eduthavanga konjam per.

Romba adhigama marks eduthavangalum konjam per.

Indha maadhiri data-la values average-ku pakkathula adhigama concentrate aagi, rendu pakkamum gradually decrease aagura pattern irundhaa, adhu Normal Distribution-oda shape-ah resemble pannalaam.

Normal Distribution-la two important terms irukku.

Mean and Standard Deviation.

Mean-na data values-oda average.

For example, five students-oda marks forty, fifty, sixty, seventy and eighty-nu irundhaa, indha values-oda average sixty.

So, mean sixty.

Standard Deviation-na data values mean-lendhu evvalavu spread aagi irukku-nguradha measure panra value.

Marks ellame sixty-ku pakkathula irundhaa spread kammi.

Sila marks romba kammi-ah irundhu, sila marks romba adhigama irundhaa spread adhigama irukkum.

Indha spread-ah understand panna Standard Deviation help pannudhu.

Normal Distribution-la Mean and Standard Deviation rendu perum important.

Mean distribution-oda centre-ah identify pannum.

Standard Deviation values evvalavu spread aagi irukku-nguradha describe pannum.

Aana ella dataset-um Normal Distribution follow pannaadhu.

Data-oda actual pattern-ah analyse pannittu dhaan endha distribution suitable-nu decide pannanum.

HOW PROBABILITY DISTRIBUTIONS HELP MACHINE LEARNING

Ippo probability distributions-ah Machine Learning-la epdi use panraanga-nu connect pannalaam.

Oru Machine Learning model customer behaviour-ah analyse pannudhu-nu imagine pannunga.

Oru customer monthly evvalavu amount spend panraar-nu data collect pannirukkom.

Different customers different amounts spend pannuvaanga.

Sila per kammiya spend pannuvaanga.

Sila per average-ah spend pannuvaanga.

Sila per adhigama spend pannuvaanga.

Indha spending values epdi distributed-ah irukku-nguradha Probability Distribution moolama analyse panna mudiyum.

Idhu customer groups-ah understand panradhukkum, unusual spending patterns-ah identify panradhukkum useful-ah irukkalaam.

Adhe maadhiri, Machine Learning models-la predictions generate panradhukkum, uncertainty-ah represent panradhukkum, data-oda statistical behaviour-ah understand panradhukkum probability concepts use aagum.

Oru model prediction kudukkumbodhu, andha prediction-oda uncertainty-ah understand panradhu important.

Yenna, real-world data always perfect-ah irukkaadhu.

Information incomplete-ah irukkalaam.

Different outcomes possible-ah irukkalaam.

Indha uncertainty-ah mathematical-ah handle panna Probability help pannudhu.

Seri, ippo namma Probability-oda basic concepts-ah different examples moolama understand pannitom.

Probability-na oru event nadakkuradhukku irukkura chance.

Conditional Probability-na oru condition pathina information already therinja situation-la innoru event nadakkuradhukku irukkura chance.

Probability Distribution-na possible values-um avatrukku irukkura probabilities-um epdi distribute aagudhu-nguradha describe panra mathematical representation.

Discrete Distribution count panna mudiyura values-ah represent pannum.

Continuous Distribution range-kulla irukkura continuous measurements-ah represent pannum.

Normal Distribution-na bell-shaped pattern follow panra oru important probability distribution.

Ippo namma oru important foundation-ah build pannitom.

Machine Learning-la Probability use panni possible outcomes and uncertainty-ah understand panna mudiyum.

Aana idhu ellame oru prediction-ku epdi lead aagudhu?

For example, oru house-oda area, bedrooms, location details-ah kuduthaa, model exact-ah house price epdi predict pannudhu?

Andha prediction oru fixed category illaama, actual numerical value-ah epdi generate pannudhu?

Indha question-ku answer therinjikka, namma next-ah Regression pathi explore panna porom.

Oru model numbers base panni pudhu values-ah predict panna epdi learn pannudhu-nguradha next lesson-la paakalaam.

Let's continue!