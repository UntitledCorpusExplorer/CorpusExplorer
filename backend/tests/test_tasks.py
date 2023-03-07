# Hack to import parent directory modules
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from bson.objectid import ObjectId
import utils, pytest, tasks



#Test cases - boundary cases and equivalence partitions
# ! Test cases for vectorize_text
# Case 1: Empty string
def test_vectorize_text_empty_string():
	old_vector = [-0.035656820982694626, -0.03319571912288666, 0.0704742893576622, 0.07324134558439255, 0.01744631864130497, -0.0014029995072633028, 0.03884357586503029, -0.050957873463630676, -0.03680857643485069, 0.04114794358611107, 0.03955468535423279, 0.04435863345861435, 0.013390855863690376, 0.038355570286512375, -0.03016854077577591, 0.05971658602356911, -0.009698532521724701, 0.0451822355389595, -0.005981894675642252, -0.019192568957805634, 0.028538988903164864, -0.016551656648516655, 0.0814380794763565, -0.01916709914803505, -0.02849951572716236, 0.05756181478500366, -0.01890493929386139, -0.09157459437847137, 0.019972514361143112, -0.0048120166175067425, -0.011466717347502708, -0.00536167761310935, 0.003469618037343025, -0.0015046701300889254, 0.047744691371917725, -0.0036930961068719625, -0.015347510576248169, 0.03967875614762306, 0.05894753336906433, -0.008169732056558132, -0.001722397399134934, -0.007212839554995298, -0.05575716495513916, 0.011524408124387264, -0.008948812261223793, 0.012736950069665909, 0.003924778662621975, -0.013687175698578358, -0.026619412004947662, -0.0293255727738142, -0.04815109074115753, 0.014419715851545334, 0.08750326931476593, 0.12123894691467285, 0.028499070554971695, 0.02604731358587742, 0.07832589000463486, 0.031571030616760254, 0.018078118562698364, -0.030918391421437263, 0.05240488797426224, 0.010864953510463238, -0.033250898122787476, 0.03656439110636711, -0.04521075636148453, -0.016698408871889114, -0.06533259898424149, -0.03448574244976044, 0.021612314507365227, 0.03863612934947014, -0.0774586945772171, 0.07058745622634888, -0.03879716619849205, 0.028113992884755135, -0.03876044228672981, -0.0018545787315815687, -0.050076618790626526, -0.018203353509306908, -0.025746263563632965, -0.03649013116955757, 0.017156796529889107, 0.06656447052955627, -0.055216673761606216, -0.000529133016243577, 0.003339147660881281, -0.00026965985307469964, -0.004434401635080576, 0.03155989572405815, 0.01385657861828804, 0.058081407099962234, -0.028943099081516266, 0.04083999618887901, 0.09120028465986252, -0.054479096084833145, 0.04065709561109543, -0.006016526836901903, 0.011862503364682198, -0.035718102008104324, 0.041426315903663635, 0.0037799212150275707, 0.03131318837404251, -0.07707517594099045, -0.025859450921416283, -0.03060675412416458, 0.041754018515348434, 0.0719231367111206, 0.025631360709667206, 0.021408258005976677, 0.04142826423048973, 0.04732368886470795, 0.044492002576589584, -0.05654970183968544, 0.013341766782104969, -0.025291401892900467, 0.007654625456780195, 0.07319881021976471, 0.0021680404897779226, -0.010307041928172112, -0.002813007216900587, -0.022443154826760292, 0.019305014982819557, 0.02371467836201191, 0.04548311233520508, 0.01757330447435379, 0.06799681484699249, 0.04242926836013794, 0.007309993728995323, -0.05427749082446098, 0.00518273189663887, 0.037081748247146606, -0.04498337581753731, 0.010945494286715984, 0.1043178141117096, 0.035094212740659714, 0.07300478965044022, 0.02905743196606636, 0.022530535236001015, -0.026277076452970505, -0.02501739375293255, -0.02817319892346859, -0.0152980862185359, 0.09092604368925095, 0.07150885462760925, -0.004807785619050264, 0.04900800436735153, -0.028073057532310486, -0.001959811430424452, 0.011734462343156338, -0.004025524947792292, 0.0031910568941384554, -0.022046755999326706, 0.0393223762512207, 0.010983642190694809, -0.038567520678043365, -0.04002293944358826, -0.055221229791641235, -0.0620681531727314, 0.055570878088474274, -0.052074186503887177, 0.008587336167693138, -0.007969735190272331, 0.006607465445995331, -0.02109704352915287, -0.04938672482967377, -0.015828685835003853, -0.007199741434305906, -0.03615386411547661, 0.018892450258135796, 0.03388069570064545, -0.036344170570373535, 0.050201866775751114, -0.030478036031126976, -0.03223753347992897, -0.030513761565089226, -0.06526856869459152, -0.006647826638072729, -0.0015134846325963736, 
     -0.03170904144644737, -0.002514573046937585, -0.007620546501129866, 0.013133578933775425, 0.013033123686909676, -0.012727188877761364, 0.04069844260811806, 0.014435227029025555, 0.053461749106645584, 0.005740842781960964, -0.056380994617938995, 0.025226371362805367, -0.04366254061460495, 0.033997729420661926, 0.03448021784424782, 0.028826048597693443, 0.05116862431168556, -0.01266864687204361, -0.1131683811545372, 0.02703922986984253, 0.015338169410824776, -0.014459259808063507, 0.023527393117547035, 0.0025145222898572683, 0.004956456832587719, -0.0055387141183018684, 0.014115815982222557, -0.017849067226052284, 0.03060556761920452, -0.006165825761854649, -0.014287487603724003, -0.05914965644478798, -0.028228256851434708, 0.013422098942101002, 0.026710277423262596, 0.11193814128637314, -0.011348347179591656, 0.014263772405683994, 0.039681244641542435, 0.07377785444259644, -0.05622703209519386, 0.030137650668621063, 0.006224772427231073, 0.008548231795430183, 0.00911233015358448, -0.028015201911330223, 0.08923978358507156, -0.04431642219424248, -0.04666449874639511, -0.04557798057794571, -0.060291435569524765, -0.040634337812662125, -0.057557497173547745, -0.013300794176757336, -0.06024665758013725, 0.030423257499933243, 0.13475710153579712, -0.07463367283344269, 0.022859379649162292, -0.05060207098722458, -0.001479506492614746, -0.014558772556483746, -0.043873708695173264, 0.003178550396114588, 0.03668808192014694, -0.04911046102643013, -0.03839973360300064, -0.034940484911203384, -0.018126459792256355, -0.026936165988445282, -0.043411754071712494, -0.052505455911159515, -0.01871403679251671, -0.006995665840804577, 0.029825249686837196, 0.037149377167224884, -0.04319941997528076, 0.027378836646676064, -0.004633542150259018, -0.051017530262470245, 0.08158643543720245, -0.031677816063165665, -0.033244747668504715, -0.0801491066813469, 0.003996393643319607, 0.0679970383644104, -0.08754881471395493, -0.0168087650090456, -0.04102536663413048, 0.01293968129903078, -0.10017858445644379, -0.008158905431628227, 0.013039779849350452, 0.05707041546702385, 0.10261339694261551, 0.002953635063022375, -0.059169311076402664, 0.0631362721323967, -0.021189771592617035, 0.024696754291653633, -0.011764755472540855, 0.1054498702287674, 0.03397712484002113, -0.03444082662463188, -0.0026767693925648928, 0.07189840823411942, 0.013830979354679585, 0.017170459032058716, 0.046149104833602905, 0.03955158591270447, 0.046582117676734924, -0.05163116380572319, 0.024818778038024902, 0.0288477074354887, -0.03846044838428497, -0.053957950323820114, -0.031199278309941292, 0.07429058104753494, 0.057717215269804, -0.02544453553855419, 0.037047211080789566, -0.042702529579401016, -0.043008748441934586, -0.0069606550969183445, -0.051827602088451385, -0.037319570779800415, 0.01653706096112728, 0.011493591591715813, 0.08268865942955017, 0.02989991195499897, 0.0013565614353865385, 0.053919509053230286, -0.026154298335313797, -0.03679398447275162, -0.09128227084875107, 0.018260113894939423, -0.04983264580368996, -0.05071565508842468, 0.008072509430348873, -0.005000811070203781, -0.0020397906191647053, 0.0188099667429924, -0.05822783708572388, 0.026875875890254974, -0.04140442982316017, 0.045411817729473114, 0.049527883529663086, 0.1203368604183197, 0.03329300135374069, -0.03866184875369072, 0.09352311491966248, 0.015302898362278938, 0.057849690318107605, -0.009775817394256592, 0.031769536435604095, -0.014362289570271969, 0.07597246021032333, -0.03061581589281559, -0.017135247588157654, 0.04008542746305466, 0.007582786027342081, 0.05232743173837662, 0.026121392846107483, -0.005536443553864956, -0.008964764885604382, 0.058574337512254715, -0.04237000271677971, 0.0008127606124617159, -0.012978087179362774, 0.016135061159729958, -0.003589285770431161, 0.040617525577545166, 0.024862634018063545, -0.0005045208963565528, -0.00035614913213066757, -0.03890435770153999, -0.022034019231796265, 0.01718044839799404, 
	 0.026221588253974915, -0.10437234491109848, -0.03353523090481758, -0.00394597090780735, -0.09325043112039566, -0.016704320907592773, -0.022325770929455757, 0.10596950352191925, -0.06410612165927887, -0.04086007550358772, 0.002209693193435669, -0.018719669431447983, -0.04493628069758415, 0.09740905463695526, -0.007012893445789814, 0.034078072756528854, -0.039601560682058334, -0.037834834307432175, -0.014830836094915867, -0.03784416615962982, 0.026697788387537003, -0.025938745588064194, 0.0016681564738973975, -0.07397560030221939, -0.10455838590860367, 0.0352238304913044, -0.00864544976502657, 0.0485193207859993, -0.06412363797426224, 0.11610011756420135, -0.09312094748020172, 0.008761310018599033, 0.008435867726802826, -0.003066824981942773, 0.04928221181035042, -0.009603464044630527, 0.031606387346982956, 0.09698472917079926, -0.0881628543138504, -0.04672500491142273, -0.06540944427251816, 0.07641193270683289, -0.022334612905979156, -0.024858834221959114, 0.04232999309897423, 0.0007309648208320141, 0.060247790068387985, 0.00792037881910801, -0.003415890736505389, -0.022191746160387993, -0.02253836765885353, 0.02691807597875595, 0.06953618675470352, 0.045719798654317856, -0.024450406432151794, -0.06548251956701279, 0.008073026314377785, -0.00804897490888834, -0.03950123116374016, -0.09169428795576096, -0.030572906136512756, -0.00017538054089527577, 0.07202281057834625, -0.016204124316573143, -0.03152402862906456, -0.03925846517086029, -0.06527188420295715, -0.027356203645467758, 0.04875662922859192, -0.07915099710226059, 0.06214980408549309, -0.039462294429540634, 0.0909096747636795, 0.013702976517379284, 0.05681123211979866, 0.03678992763161659, 0.03107033111155033, -0.045738451182842255, -0.048064932227134705, 0.037249498069286346, 0.03552229702472687, 0.06067144498229027, 0.010426533408463001, -0.014573811553418636, 0.10037625581026077, 0.00032426390680484474, 0.0008006887510418892, 0.11466469615697861, 0.03898308053612709, 0.013250522315502167, -0.028330018743872643, 0.018508203327655792, -0.007735402323305607, 0.017201155424118042, -0.05883427709341049, -0.015495173633098602, -0.02924976497888565, -0.032818712294101715, -0.03175950422883034, 0.0019346143817529082, 0.031020674854516983, -0.009644027799367905, -0.028078719973564148, -0.0017032456817105412, 0.024866275489330292, -0.008941599167883396, 0.020764611661434174, 7.551406451966614e-05, 0.021432099863886833, 0.06986009329557419, 0.05725659057497978, 0.008021940477192402, -0.04002108424901962, -0.009625070728361607, 0.0535457469522953, 0.024066956713795662, -0.034008532762527466, 0.02898385003209114, 0.05670391395688057, 0.09739216417074203, 0.0172662865370512, -0.007439596112817526, 0.044582415372133255, 0.03726250305771828, 0.04264943301677704, 0.007573893293738365, -0.02050880528986454, 0.02652616798877716, -0.076387919485569, -0.0035039354115724564, 0.022623348981142044, -0.06134151667356491, -0.0019699770491570234, -0.020724913105368614, 0.04803844913840294, 0.006185242440551519, 0.013777771033346653, -0.08737826347351074, 0.058049526065588, 0.006630798801779747, 0.031414881348609924, 0.06902438402175903, -0.058781154453754425, 0.07402253150939941, 0.004315294325351715, 0.03831944614648819, 0.04681685194373131, 0.04271106794476509, -0.10958446562290192, 0.017249900847673416, -0.012399083003401756, -0.04777942970395088, -0.012182744219899178, -0.08347323536872864, -0.0636080801486969, -0.020792953670024872, -0.022509673610329628]
	new_vector = tasks.vectorize_text([""])
	for o in range(len(new_vector)):
		assert new_vector[o] == old_vector[o]
	
# Case 2: single string
def test_vectorize_text_first_item():
	session, db = utils.create_transaction_session()
	document = db.documents.find_one({"_id": ObjectId("637eabe7f0a9482a337a11d5")})
	old_vector = document["textVector"]
	new_vector = tasks.vectorize_text([document["text"]])
	for o in range(len(new_vector)):
		assert new_vector[o] == old_vector[o]

# Case 3: multiple string
def test_vectorize_text_second_item():
	session, db = utils.create_transaction_session()
	document = db.documents.find_one({"_id": ObjectId("637eae8a0381748b89ae518a")})
	old_vector = document["textVector"]
	new_vector = tasks.vectorize_text([document["text"]])
	for o in range(len(new_vector)):
		assert new_vector[o] == old_vector[o]

	
# Test cases for vectorize_document
# Case 1: invalid document id
def test_vectorize_invalid_document_id():
	with pytest.raises(Exception):
		tasks.vectorize_document((), document_id = '42')
	

# Case 2: Valid document id in mongodb
def test_vectorize_document_id_in_database():
	session, db = utils.create_transaction_session()
	document = db.documents.find_one({"_id": ObjectId("637eabe7f0a9482a337a11d5")})
	old_vector = document['textVector']
	new_vectorized_document = tasks.vectorize_document(document)
	new_vector = new_vectorized_document['textVector']
	for o in range(len(new_vector)):
		assert new_vector[o] == old_vector[o]

# Test cases for create_child
# Case 1: invalid document id
def test_create_child_invalid_document_id():
	with pytest.raises(Exception):
		tasks.create_child((), start_index = 2, end_index = 40, document_id = '30')

#Case 2: valid document id
#TODO: Clean up the database for whatever changes you've made once the test is over (The test_tasks that were there before)
def test_create_child_valid_document():
	start = 48
	end = 100
	session, db = utils.create_transaction_session()
	reddit_id, id = tasks.create_child(start_index = start, end_index = end, document_id = '637eabe7f0a9482a337a11d5')
	try:
		document_id = "637eabe7f0a9482a337a11d5"
		document = db.documents.find_one({"_id": ObjectId("637eabe7f0a9482a337a11d5")})
		# reddit_id = document["id"]
		assert reddit_id == f"{document_id}#{str(start)}#{str(end)}"
	finally:
		db.documents.delete_one({'_id': id})
#Case 3: valid document id, end_index outside range of document
def test_create_child_outside_document_range():
	start = 0
	end = 100000000
	session, db = utils.create_transaction_session()
	with pytest.raises(Exception):
		tasks.create_child((), start_index = start, end_index = end, document_id = ObjectId("637eabe7f0a9482a337a11d5"))