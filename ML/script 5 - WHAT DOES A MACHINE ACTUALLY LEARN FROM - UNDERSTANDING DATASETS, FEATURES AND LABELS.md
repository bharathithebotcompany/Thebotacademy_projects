PART FIVE – WHAT DOES A MACHINE ACTUALLY LEARN FROM? UNDERSTANDING DATASETS, FEATURES AND LABELS

Last part-la Machine Learning-oda three major learning approaches-ah understand pannom.

Supervised Learning, Unsupervised Learning and Reinforcement Learning.

Indha approaches ellathulayum data romba important role play pannudhu-nu paathom.

Aana ippo namma oru basic question-ku answer therinjikkanum.

Machine Learning model-ku data provide panrom-nu solrom.

Aana andha data epdi irukkum?

Adhula enna information irukkum?

Computer andha information-ah epdi use panni learn pannum?

Idha understand panna, first Dataset-na enna-nu paakalaam.

What Is a Dataset?

Simple-ah sollanumna, oru particular purpose-ku collect panni organize pannina related information-oda collection dhaan Dataset.

For example, oru real estate company houses sell panraanga-nu imagine pannunga.

Andha company-kitta different houses pathina information irukku.

Each house-oda location, area, bedrooms count and selling price maadhiri details collect panni vechirukkaanga.

Indha information ellathayum organize panni store panninaa, adhu oru dataset-ah maarum.

Inga important-ah understand panna vendiya vishayam enna-na, dataset-na just random information illa.

Oru particular problem-ah solve panna useful-ah irukkura related data organized-ah irukkanum.

Machine Learning-la model learn panna use panra information indha dataset-la dhaan irukkum.

Understanding Rows and Columns

Ippo oru dataset epdi organize aagudhu-nu paakalaam.

Usually, beginner-level Machine Learning projects-la data table format-la irukkum.

Indha table-la rows and columns irukkum.

First, Row-na enna?

Oru row-na dataset-la irukkura oru individual record or example.

Namma house dataset-ah consider pannunga.

First row-la oru house-oda details irukkum.

Second row-la innoru house-oda details irukkum.

Third row-la vera oru house-oda details irukkum.

Ippadi ovvoru row-um oru individual house pathina information-ah represent pannum.

Ippo Column-na enna?

Column-na ovvoru record-um share panra particular type of information-ah represent pannum.

For example, namma dataset-la location, area, bedrooms and price-nu columns irukkalaam.

Location column-la houses-oda location details irukkum.

Area column-la house-oda size details irukkum.

Bedrooms column-la bedroom count irukkum.

Price column-la selling price irukkum.

So, rows individual records-ah represent pannum.

Columns andha records-la collect pannina different types of information-ah represent pannum.

Indha structure-ah understand panninaa, dataset-la irukkura information-ah read panradhu easy-ah irukkum.

What Are Features?

Ippo Machine Learning-la romba important-ah use aagura oru term-ku varalaam.

Adhu dhaan Features.

Feature-na enna?

Oru data example-ah describe panna help panra individual characteristic or information-ku Feature-nu peru.

Namma house dataset-la location, area and bedrooms ellame features.

Because indha information house-oda characteristics-ah describe pannudhu.

Ippo oru house price predict pannanum-nu imagine pannunga.

Andha house evvalavu perusa irukku?

Endha location-la irukku?

Evvalavu bedrooms irukku?

Indha information ellame house-oda expected price-ah estimate panna useful-ah irukkalaam.

So, Machine Learning model indha features-ah analyse panni, house price-oda relationship-ah learn panna try pannum.

Inga oru important point.

Features-na model-ku provide panra input information.

Ovvoru feature-um model-ku oru particular detail-ah provide pannum.

Model indha details-ah use panni patterns identify pannum.

What Are Labels?

Ippo features purinjikittom.

Next, Labels-na enna-nu paakalaam.

Label-na Supervised Learning-la oru data example-ku corresponding-ah irukkura correct answer or target value.

Namma house price prediction example-ah continue pannalaam.

Dataset-la location, area and bedrooms details irukku.

Adhe dataset-la ovvoru house-um actual-ah evvalavu price-ku sell aachu-ngura information-um irukku.

Inga location, area and bedrooms features.

Actual selling price dhaan label.

Because namma model-kitta predict panna solla pora answer adhu dhaan.

Ippo model training time-la house-oda features-um, adhoda actual selling price-um provide panrom.

Model indha information-la irundhu relationship learn panna try pannum.

Training mudinja apram, previously paakaadha oru house-oda location, area and bedrooms details mattum provide panrom.

Appo model expected selling price-ah predict panna try pannum.

Inga new house-oda actual selling price namakku innum theriyadhu.

Adhanaala prediction generate panna model learn pannina patterns-ah use pannum.

So, features are the inputs.

Label is the answer that the model is expected to learn to predict.

Idhu Supervised Learning-la romba important concept.

How Do Features and Labels Work Together?

Ippo features and labels rendu terms-um separate-ah understand pannitom.

Aana ivanga rendu perum epdi connect aagudhu-nu paakalaam.

Namma dataset-la ovvoru house-ukkum features and label irukkum.

Features house-oda details-ah describe pannum.

Label andha house-oda actual selling price-ah represent pannum.

Model indha examples-ah observe panni, features and label-kku idaiyila irukkura relationship-ah learn panna try pannum.

For example, house area increase aagumbodhu price epdi change aagudhu?

Different locations-la irukkura houses-oda prices epdi differ aagudhu?

Bedrooms count price-ah influence pannudha?

Indha maadhiri relationships-ah dataset-la irundhu model identify panna try pannum.

Aana model oru single feature-ah mattum base panni decision edukka vendiyadhu illa.

Multiple features-ah serthu analyse pannalaam.

Andha features ellathayum consider panni output generate panna model learn pannum.

Idhu dhaan features and labels serndhu Machine Learning training-la work panra basic idea.

Different Types of Data in a Dataset

Ippo dataset-la enna information irukkum-nu paathom.

Aana ella data-um ore format-la irukkaadhu.

Machine Learning-la data different types-la irukkalaam.

Beginner stage-la two important types-ah understand pannalaam.

Numerical Data and Categorical Data.

First, Numerical Data.

Numerical data-na numbers format-la represent panra information.

Namma house dataset-la area, bedrooms count and selling price maadhiri values numerical data-ah irukkalaam.

For example, house area thousand square feet-ah irukkalaam.

Bedrooms count three-ah irukkalaam.

Selling price fifty lakhs-ah irukkalaam.

Indha values ellame numbers moolama represent pannappadudhu.

Ippo Categorical Data.

Categorical data-na information-ah different groups or categories moolama represent panradhu.

Namma same house dataset-la location or property type maadhiri information categorical data-ah irukkalaam.

For example, location Chennai, Bengaluru or Hyderabad-ah irukkalaam.

Property type apartment, independent house or villa-ah irukkalaam.

Inga information categories or names moolama represent pannappadudhu.

So, numerical data numbers-ah represent pannum.

Categorical data different categories-ah represent pannum.

Indha difference important.

Because Machine Learning models different types of data-ah process panna different preparation methods thevaippadalaam.

Adha namma data preparation lesson-la detailed-ah paaka porom.

Are All Features and Labels the Same in Every Problem?

Ippo oru important clarification.

Oru dataset-la endha column feature-ah irukkanum, endha column label-ah irukkanum-nguradhu fixed-ah irukkaadhu.

Namma solve panna pora problem-ah depend pannum.

Same dataset-ah different problems-ku use panna mudiyum.

For example, namma house dataset-la location, area, bedrooms and selling price irukku.

House price predict pannanum-na selling price label-ah irukkum.

Aana house price already known-ah irukku, andha house expensive category-ah illa affordable category-ah-nu classify pannanum-na, namma predict panna pora category dhaan label-ah maarum.

For example, selling price-ah base panni houses-ah expensive and affordable-nu categories-ah divide panni, andha category-ah predict panna model train pannalaam.

So, feature and label roles depend on the prediction task.

Dataset-la irukkura oru column always feature-ah dhaan irukkanum or label-ah dhaan irukkanum-nu avasiyam illa.

Problem change aagumbodhu, namma choose panra target-um change aagalaam.

What Happens When We Don't Have Labels?

Ippo varaikkum namma features and labels pathi Supervised Learning context-la understand pannom.

Aana Unsupervised Learning-la labels irukkaadhu-nu Part Four-la paathom.

Appo features irukkumaa?

Yes.

Unsupervised Learning-layum model-ku data features provide pannalaam.

Aana correct answer or target label provide panna maattom.

For example, customer information-la purchase frequency, spending amount and product preferences maadhiri features irukkalaam.

Aana indha customers endha group-ku belong aaguraanga-nu pre-defined label irukkaadhu.

Model indha features-ah analyse panni similarities identify panna try pannum.

So, features are useful input information.

Labels are correct answers or target values used in Supervised Learning.

Indha difference-ah clear-ah understand pannikkonga.

Why Does Data Structure Matter?

Ippo namma dataset, rows, columns, features and labels ellathayum understand pannitom.

Aana idhellam Machine Learning-ku edhukku important?

Because model-ku data provide panradhu mattum podhaadhu.

Andha data-la enna information irukku, adhu epdi organized-ah irukku, model-ku endha information useful-ah irukku-nu namakku theriyanum.

Features-la unnecessary or irrelevant information irundhaa model-ku useful patterns identify panradhu difficult-ah irukkalaam.

Labels incorrect-ah irundhaa Supervised Learning model wrong information-la irundhu learn pannalaam.

Dataset-la missing values or duplicate records irundhaalum training affect aagalaam.

Adhanaala model train panradhukku munnadi data-ah properly understand pannanum.

Data quality-um data structure-um Machine Learning-la important role play pannudhu.

Ippo namma next lesson-la indha data-ah prepare panradhu pathi paaka porom.

Okay!

Indha lesson-la namma important-ah understand pannina concepts-ah recap pannalaam.

Dataset-na related information organized-ah collect pannina oru collection.

Rows-na dataset-la irukkura individual records or examples.

Columns-na ovvoru record-la irukkura different types of information.

Features-na model-ku provide panra input characteristics.

Labels-na Supervised Learning-la model predict panna learn panra correct answers or target values.

Numerical data-na numbers format-la irukkura information.

Categorical data-na different groups or categories-ah represent panra information.

Same dataset-la features and labels enna-nguradhu namma solve panna pora problem-ah depend pannum.

Indha concepts ellame Machine Learning-ku data-ah understand panna foundation-ah irukkum.

Ippo namma next important question-ku varalaam.

Oru dataset collect pannitom.

Adhula rows irukku, columns irukku, features and labels-um irukku.

Appo andha data-ah direct-ah Machine Learning model-ku provide pannidalaamaa?

Ella values-um correct-ah irukkumaa?

Missing information irundhaa enna pannuvom?

Different formats-la irukkura values-ah epdi handle pannuvom?

Numbers romba different ranges-la irundhaa enna nadakkum?

Indha problems ellathayum solve panradhukku data preparation thevai.

Adha dhaan next part-la beginning-lendhu understand panna porom.

Let's continue!