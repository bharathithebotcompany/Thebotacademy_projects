PART SIX – BEFORE A MACHINE CAN LEARN, HOW DO WE PREPARE THE DATA?

Last part-la namma Dataset, Rows, Columns, Features and Labels pathi understand pannom.

Machine Learning model-ku data provide panradhu mattum podhaadhu.

Andha data properly organized-ah irukkanum. Model learn panradhukku useful-ah irukkanum.

Aana real-world-la collect panra data ellame perfect-ah irukkaadhu.

Sometimes information missing-ah irukkalaam.

Same record multiple times repeat aagalaam.

Different formats-la values store aagirukkalaam.

Some values romba different ranges-la irukkalaam.

Indha maadhiri problems irundhaa, model data-la irundhu correct patterns learn panradhu difficult-ah aagalaam.

Adhanaala model train panradhukku munnadi data-ah prepare pannanum.

Indha process-ku dhaan Data Preprocessing or Data Preparation-nu peru.

Data Preprocessing-na raw data-ah model use panna suitable-ah clean panni, organize panni, transform panra process.

Ippo idhu edhukku thevai, epdi work aagudhu-nu step by step understand pannalaam.

Why Do We Need Data Cleaning?

First, Data Cleaning.

Data Cleaning-na dataset-la irukkura mistakes, missing information and unnecessary records-ah identify panni handle panradhu.

Idha same house price dataset use panni understand pannalaam.

Suppose oru real estate company-kitta thousands of houses-oda details irukku.

Andha dataset-la location, area, bedrooms and selling price details irukku.

Aana data collect pannumbodhu sila problems irukku.

Oru house-oda area value missing-ah irukku.

Innorutharoda selling price enter pannama vitturukkaanga.

Same house details accidentally two times record aagirukku.

Innum sila records-la location name different spelling-la enter pannirukkaanga.

Indha problems ellame model training-ah affect pannalaam.

So, first namma missing values-ah handle pannanum.

Duplicate records-ah identify pannanum.

Inconsistent information-ah correct pannanum.

Idhellam Data Cleaning-oda part.

Handling Missing Values

Ippo Missing Values-na enna-nu paakalaam.

Missing Value-na dataset-la oru particular field-ku required information available-ah illaama irukkuradhu.

For example, house dataset-la oru house-oda area value missing-ah irukkalaam.

Ippo indha missing value-ku enna pannalaam?

Adha appadiye leave pannalaamaa?

Illai remove pannidalaamaa?

Actually, adhu situation-ah depend pannum.

Missing information irukkura record romba important illa-na, andha record-ah remove panradhu oru option-ah irukkalaam.

Aana record important-ah irundhaa, missing value-ah suitable method use panni fill pannalaam.

Indha process-ku Imputation-nu peru.

Imputation-na missing values-ku appropriate replacement values provide panradhu.

For example, house area values-la missing information irundhaa, available house area values-oda average use panni fill panna mudiyum.

Average-na ella numerical values-um add panni, total number of values-la divide panra calculation.

Suppose three houses-oda areas thousand, twelve hundred and fourteen hundred square feet-nu irukku.

Indha values-oda average twelve hundred square feet.

So, missing area value-ku twelve hundred-nu fill panna oru simple approach use pannalaam.

Aana idhu every situation-layum correct-ah irukkum-nu solla mudiyadhu.

Missing value endha column-la irukku, data eppadi distributed-ah irukku, andha information evvalavu important-nu consider panni method select pannanum.

Removing Duplicate and Incorrect Data

Next, Duplicate Records.

Duplicate-na same information accidentally multiple times dataset-la appear aaguradhu.

For example, same house details rendu rows-la repeat aagirukku-nu imagine pannunga.

Andha duplicate records remove pannalaam.

Because same information repeated-ah irundhaa, certain patterns dataset-la actual-ah irukkuradha vida adhigama represent aagalaam.

Next, Inconsistent Data.

Inconsistent data-na same type of information different formats or spellings-la store aagirukkuradhu.

For example, location column-la Chennai-nu oru record-la irukku.

Innorutharoda record-la chennai-nu small letters-la irukku.

Innum oru record-la Chennai city-nu irukku.

Indha values ellame same location-ah represent pannudhu-na, namma consistent format-ku convert pannanum.

Appo model-ku same information different categories maadhiri confuse aagura chance reduce aagum.

So, missing values, duplicates and inconsistent records-ah handle panradhu data cleaning-la important steps.

Converting Categorical Data into Numbers

Ippo data clean pannitom.

Aana innum oru important problem irukku.

Machine Learning models-ku categorical information-ah epdi provide panradhu?

Namma house dataset-la location column irukku-nu imagine pannunga.

Adhula Chennai, Bengaluru and Hyderabad maadhiri values irukkalaam.

Indha values text format-la irukku.

Many Machine Learning algorithms numerical representations-ah use panni calculations perform pannum.

So, categorical values-ah suitable numerical format-ku convert panna vendiyirukkum.

Indha process-ku Encoding-nu peru.

Encoding-na categorical information-ah machine learning model process panna suitable numerical representation-ah convert panradhu.

Idhula oru simple method One-Hot Encoding.

One-Hot Encoding-na oru category irukkaa illaiyaa-nu represent panna separate binary columns create panradhu.

Binary-na two possible values mattum irukkura format. Usually zero and one.

Namma location example-la Chennai, Bengaluru and Hyderabad-nu three categories irukku.

One-Hot Encoding apply panninaa, indha three locations-kum separate columns create pannalaam.

Oru house Chennai-la irundhaa, Chennai column-la one irukkum.

Bengaluru and Hyderabad columns-la zero irukkum.

Ippadi category information-ah zero and one use panni represent panrom.

Idhu categorical data-ah numerical format-ku convert panna use aagura oru common method.

Aana encoding-ku different methods irukku.

Endha method use pannanum-nguradhu categories-oda nature and problem-ah depend pannum.

Why Do We Need Feature Scaling?

Ippo categorical data-ah numerical format-ku convert panradhu purinjikittom.

Next, numerical features pathi oru important concept paakalaam.

Adhu dhaan Feature Scaling.

Feature Scaling-na different numerical features-oda value ranges-ah suitable scale-ku kondu varra process.

Idhu edhukku thevai?

Namma house dataset-la two features irukku-nu imagine pannunga.

House area and number of bedrooms.

Area values thousands-la irukkalaam.

Bedrooms values one, two, three or four maadhiri small numbers-ah irukkalaam.

Ippo indha two features-um romba different ranges-la irukku.

Sila Machine Learning algorithms-la, indha difference model calculations and learning process-ah affect pannalaam.

Adhanaala certain algorithms use pannumbodhu Feature Scaling helpful-ah irukkum.

Feature Scaling-ku oru common method Standardization.

Standardization-na numerical values-ah avanga original scale-la irundhu, mean zero and standard deviation one irukkura scale-ku transform panradhu.

Mean-na values-oda average.

Standard Deviation-na values average-lendhu evvalavu spread aagirukku-nguradha measure panra oru statistical value.

Ippo indha terms konjam technical-ah irukkalaam.

Inga detailed mathematics-ku pogama, Standardization different numerical features-ah comparable scale-ku kondu vara help pannudhu-nu understand pannikkonga.

Innor u common method Min-Max Scaling.

Min-Max Scaling-na values-ah usually zero and one-kku idaiyila map panradhu.

For example, original feature-la minimum value zero and maximum value hundred-na, scaled values zero-lendhu one varaikkum represent aagalaam.

Feature Scaling ella algorithms-ukkum compulsory illa.

Some algorithms feature values-oda scale-ku sensitive-ah irukkum.

Innum sila algorithms-ku scaling perusa thevai padaadhu.

So, namma use panra model-ah base panni scaling decide pannanum.

Splitting the Dataset for Training and Testing

Ippo namma data clean pannitom.

Categorical values-ah encode pannitom.

Thevaiyaana features-ku scaling-um apply pannitom.

Next, model train panradhukku munnadi dataset-ah separate parts-ah divide pannanum.

Indha process-ku Train-Test Split-nu peru.

Train-Test Split-na available dataset-ah training data and testing data-nu separate-ah divide panradhu.

Idhu edhukku thevai?

Namma model-ku house examples provide panni train panrom-nu imagine pannunga.

Model already paatha houses-la irundhu patterns learn pannum.

Aana training-la use pannina same houses-ah thirumba kuduthu test panninaa, model new information-ku epdi perform pannum-nu properly evaluate panna mudiyadhu.

Adhanaala dataset-la oru portion training-ku use panrom.

Innor u separate portion testing-ku reserve panrom.

Training data use panni model patterns learn pannum.

Testing data use panni, model previously paakaadha examples-la epdi perform pannudhu-nu evaluate panrom.

For example, dataset-la ten thousand records irundhaa, eighty percent training-ku and twenty percent testing-ku divide pannalaam.

Inga eighty-twenty ratio oru common example mattum dhaan.

Ella projects-layum idhe ratio use pannanum-nu avasiyam illa.

Dataset size and project requirements-ah base panni split ratio change aagalaam.

Innum oru important point.

Training, validation and testing-nu three separate datasets use panra approach-um irukku.

Validation data model training process-la settings or configurations select panna help pannum.

Testing data final evaluation-ku use aagum.

Training and testing difference-ah namma later lessons-la innum detailed-ah understand pannuvom.

What Is Data Leakage?

Train-Test Split pathi pesumbodhu, oru important problem-ah kandippa understand pannanum.

Adhu dhaan Data Leakage.

Data Leakage-na model train aagumbodhu, prediction time-la normally available-ah irukka koodaadha information training process-kulla enter aaguradhu.

Idha oru simple example moolama understand pannalaam.

Namma house price predict panra model create panrom-nu imagine pannunga.

Model-ku house area, location and bedrooms details provide panrom.

Aana data preparation time-la actual selling price information-um accidentally input features-kulla include aagiduchu.

Ippo model training time-la correct price-ah indirectly paathudum.

Adhanaala training-la model romba accurate-ah perform panra maadhiri theriyalaam.

Aana real-world-la new house price predict pannumbodhu actual selling price already available-ah irukkaadhu.

So, model expected information illama prediction generate panna struggle pannalaam.

Idhu dhaan Data Leakage-oda basic problem.

Data Leakage avoid panradhu romba important.

Training time-la model-ku provide panra information, actual prediction time-la available-ah irukkura information-ah dhaan represent pannanum.

Data preparation steps-um training and testing data separation-ah respect panni perform pannanum.

For example, missing values fill panradhukku use panra average or feature scaling parameters-ah training data-lendhu learn panni, adhe values-ah testing data-kum apply pannanum.

Testing data information use panni preparation rules learn panninaa leakage nadakka chance irukku.

Idha practical-ah implement panradhu namma coding session-la paaka porom.

Is Data Preparation Always the Same?

Ippo data preparation-la important steps-ah understand pannitom.

Aana ella Machine Learning projects-layum indha steps ellame same order-la, same method-la use pannanum-nu avasiyam illa.

Problem enna, dataset-la enna issues irukku, endha algorithm use panrom-nguradha base panni preparation steps change aagalaam.

For example, dataset-la missing values illaina missing value imputation thevai padaadhu.

Categorical features illaina encoding thevai padaadhu.

Feature scaling thevai padaadha algorithm use panninaa, scaling skip pannalaam.

So, data preparation-na blindly ellaa steps-um apply panradhu illa.

Dataset-ah understand panni, actual-ah irukkura problems-ku suitable solutions select panradhu dhaan important.

Lesson Recap and Transition

Okay!

Indha lesson-la namma Data Preparation-oda important concepts-ah understand pannitom.

Data Preprocessing-na raw data-ah Machine Learning-ku suitable-ah prepare panra process.

Data Cleaning-na missing values, duplicate records and inconsistent information-ah handle panradhu.

Imputation-na missing values-ku suitable replacement values provide panradhu.

Encoding-na categorical information-ah numerical representation-ku convert panradhu.

Feature Scaling-na numerical features-ah suitable scale-ku kondu varradhu.

Train-Test Split-na model training and testing-ku dataset-ah separate-ah divide panradhu.

Data Leakage-na model training time-la inappropriate information use aagi, evaluation misleading-ah maaruradhu.

Indha steps ellame model-ku better quality data provide panna help pannum.

Ippo namma data collect panradhu and prepare panradhu rendaiyum understand pannitom.

Next question enna?

Indha prepared dataset-ah model-kitta provide panninaa, actual-ah learning process epdi start aagum?

Model first enna pannum?

Prediction generate panradhu-na enna?

Mistake nadandhaa model epdi improve aagum?

Training process-la parameters and error enna role play pannum?

Indha questions-ku answer next part-la paaka porom.

Because data preparation mudinja piragu, Machine Learning-oda most important process  Model Training  epdi work aagudhu-nu understand panna porom.

Let's continue!