# USAGE
# python train_request.py

# import the necessary packages
import requests
import datetime

# initialize the Keras REST API endpoint to train
# the port number must the number you set
KERAS_REST_API_URL = "http://localhost:4321/train"


# set spam editor accounts with non_spam verdict details to retrain the model
training_data = {}

training_data[0] = {
    'verdict' : 0, #set as non_spam
    'id' : 1,
    'email': 'ghhfbca@porsh.net',
    'website': 'http://www.kisaiya.co.uk',
    'bio': 'skill seo brush seo fish seo verify seo kangaroo seo obey seo ecology seo abandon seo keep seo other seo private seo skirt seo gallery seo tilt seo castle seo crew seo celery seo fiber seo dog seo scatter seo library seo impose seo noise seo autumn seo exclude seo renew seo digital seo robot seo naive seo recipe seo connect seo flock seo canoe seo miracle seo arctic seo velvet seo mimic seo vague seo always seo combine seo enroll seo napkin seo save seo require seo seat seo sign seo desert seo other seo powder seo laundry seo source seo shiver seo region seo frost seo combine seo mushroom seo easily seo call seo reason seo horror seo deal seo enemy seo lend seo exile seo route seo grid seo jeans seo steel seo attack seo stage seo squeeze seo lobster seo snow seo save seo smooth seo save seo depend seo subway seo cheese seo minimum seo kangaroo seo craft seo pyramid seo work seo bus seo run seo drama seo need seo ankle seo time seo frozen seo inquiry seo awake seo method seo kit seo october seo desert seo crowd seo strong seo report seo love seo cute seo subway seo flush seo latin seo extend seo rabbit seo half seo cement seo cushion seo volcano seo gaze seo model seo laptop seo reject seo run seo talk seo device seo ready seo receive seo output seo always seo ankle seo seek seo produce seo flock seo ripple seo timber seo horror seo account seo peanut seo tide seo fragile seo silk seo hover seo enrich seo reject seo century seo bamboo seo fabric seo approve seo cupboard seo gap seo diagram seo recall seo minor seo certain seo skirt seo castle seo expect seo oven seo palace seo zone seo few seo ring seo stem seo online seo sketch seo gossip seo innocent seo uncover seo deliver seo ensure seo middle seo tornado seo lunar seo latin seo essay seo negative seo skull seo crystal seo ugly seo then seo insane seo police seo arrive seo ginger seo half seo shoulder seo gloom seo size seo accident seo enact seo diet seo reopen seo best seo screen seo joke seo height seo awful seo notice seo bulk seo civil seo bubble seo hockey seo devote seo tape seo sword seo century seo explain seo lesson seo cry seo govern seo decrease seo bonus seo girl seo slogan seo estate seo bacon seo slam seo diesel seo series seo program seo scout seo curious seo tenant seo mimic seo session seo share seo clarify seo suffer seo rival seo area seo measure seo profit seo shove seo curtain seo answer seo enhance seo blade seo firm seo lend seo distance seo horror seo plunge seo public seo almost seo champion seo color seo blue seo gas seo soup seo multiply seo razor seo increase seo skin seo belt seo diesel seo trust seo butter seo celery seo hat seo honey seo mask seo magic seo sense seo galaxy seo elite seo luggage seo replace seo visit seo sail seo decline seo ghost seo claim seo jazz seo exchange seo video seo around seo item seo grunt seo rural seo zoo seo strategy seo glue seo shell seo ancient seo hockey seo legal seo fuel seo future seo  www.spam.org  www.spam.org  www.spam.org ',
    'area': None,
    'privs': 0,
    'gender': 'gender',
    'birth_date': datetime.datetime(2000, 7, 5, 14, 22, 8, 5).strftime('%Y-%m-%dT%H:%M:%S'), #strftime to make json serializable
    'member_since': datetime.datetime(2000, 9, 2, 5, 19, 1, 5).strftime('%Y-%m-%dT%H:%M:%S'),
    'email_confirm_date': datetime.datetime(2000, 9, 3, 6, 58, 54, 5).strftime('%Y-%m-%dT%H:%M:%S'),
    'last_updated': datetime.datetime(2000, 9, 2, 7, 21, 8, 5).strftime('%Y-%m-%dT%H:%M:%S'),
    'last_login_date': datetime.datetime(2000, 9, 2, 9, 21, 38, 5).strftime('%Y-%m-%dT%H:%M:%S'),
    }

training_data[1] = {
        'verdict' : 0, #set as non_spam
        'id' : 2,
        'email': 'eblldga@buysteroids365.com',
        'website': 'http://bit.ly',
        'bio': 'swap seo town seo scare seo vital seo tomato seo idle seo impact seo boil seo beef seo baby seo idle seo wrist seo identify seo yellow seo nation seo city seo segment seo ramp seo era seo surface seo borrow seo young seo immune seo better seo license seo hundred seo cannon seo catch seo razor seo ecology seo before seo lamp seo elbow seo memory seo lizard seo job seo news seo insect seo fold seo main seo diary seo banana seo grant seo repeat seo patch seo recycle seo affair seo fox seo please seo anchor seo inch seo utility seo fiscal seo spawn seo explain seo sweet seo still seo sponsor seo shoe seo tobacco seo north seo room seo smile seo outdoor seo expire seo useless seo ski seo alien seo shift seo dose seo badge seo assault seo reject seo agree seo kiss seo trim seo effort seo fossil seo age seo assault seo frown seo owner seo amateur seo original seo control seo adult seo cruel seo domain seo space seo vault seo latin seo salt seo guide seo wage seo mosquito seo wool seo panther seo will seo bid seo scrub seo click seo purpose seo invest seo useful seo camera seo earth seo name seo acquire seo now seo can seo job seo topple seo drama seo sister seo table seo window seo hockey seo fury seo offer seo imitate seo erase seo crash seo concert seo detail seo universe seo hope seo dolphin seo detail seo fury seo essay seo garlic seo noodle seo merry seo popular seo luxury seo agree seo drama seo bracket seo genre seo indicate seo economy seo maple seo wage seo limb seo because seo legal seo magic seo genius seo medal seo crawl seo evolve seo pyramid seo cake seo diary seo achieve seo frame seo attend seo crush seo bronze seo silk seo code seo draw seo radar seo cluster seo gate seo garage seo ceiling seo clap seo undo seo program seo trust seo speed seo glory seo teach seo harbor seo order seo fine seo unaware seo great seo rubber seo lava seo sea seo advance seo inmate seo ill seo cushion seo illegal seo breeze seo hurry seo emotion seo fine seo love seo rely seo deny seo inspire seo payment seo system seo recycle seo sibling seo raw seo funny seo trend seo alter seo muscle seo legal seo typical seo aunt seo lion seo soldier seo balcony seo repeat seo below seo space seo reward seo core seo attack seo basic seo thunder seo address seo note seo medal seo wool seo omit seo clerk seo paddle seo coach seo flight seo above seo genius seo twelve seo arrest seo isolate seo casino seo blood seo never seo charge seo bunker seo goddess seo real seo lend seo crash seo relax seo raise seo shy seo army seo claim seo nasty seo require seo month seo clip seo dust seo dish seo peasant seo account seo method seo auto seo economy seo trophy seo curve seo gadget seo setup seo repeat seo match seo bargain seo wagon seo pole seo purse seo arctic seo bar seo noble seo dove seo nature seo join seo crouch seo term seo behave seo scare seo birth seo decide seo fan seo pair seo broom seo lecture seo ketchup seo vast seo that seo orient seo matrix seo width seo agent seo ozone seo tube seo next seo veteran seo damp seo enlist seo model seo palm seo disorder seo bonus seo smile seo dynamic seo autumn seo buddy seo muffin seo base seo confirm seo material seo member seo glue seo work seo sunset seo expand seo affair seo setup seo family seo fee seo again seo pause seo aware seo original seo oven seo observe seo piano seo whip seo pumpkin seo history seo rather seo across seo cotton seo edge seo differ seo betray seo one seo robot seo reject seo catch seo spy seo parent seo organ seo rival seo mirror seo walk seo fashion seo steak seo fiscal seo young seo lounge seo satoshi seo entry seo civil seo squirrel seo fitness seo put seo random seo custom seo chuckle seo relief seo steak seo fine seo visual seo olympic seo lunar seo love seo where seo flip seo between seo focus seo antenna seo shop seo climb seo mandate seo shoe seo reject seo hawk seo suffer seo chalk seo recycle seo exchange seo stem seo oval seo work seo cabbage seo hurry seo motion seo dignity seo token seo weapon seo acquire seo call seo mystery seo until seo ',
        'area': None,
        'privs': 0,
        'gender': 'gender',
        'birth_date': None,
        'member_since': datetime.datetime(2018, 12, 28, 0, 3, 35, 5).strftime('%Y-%m-%dT%H:%M:%S'), #strftime to make json serializable
        'email_confirm_date': datetime.datetime(2018, 12, 29, 2, 29, 6, 5).strftime('%Y-%m-%dT%H:%M:%S'),
        'last_updated': None,
        'last_login_date': datetime.datetime(2018, 12, 28, 20, 25, 53, 5).strftime('%Y-%m-%dT%H:%M:%S'),
    }

# seding request to /train end-point of the API
r = requests.post(KERAS_REST_API_URL,json = training_data).json()

if r["success"]:
   print(r)

# otherwise, the request failed
else:
    print("Request failed")

