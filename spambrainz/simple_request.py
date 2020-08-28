# USAGE
# python simple_request.py

# import the necessary packages
import requests
import datetime
# initialize the Keras REST API endpoint URL along with the input
# image path
KERAS_REST_API_URL = "http://localhost:5000/predict"


# load the input image and construct the payload for the request

editor_account = {
    
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
    'last_login_date': datetime.datetime(2000, 9, 2, 9, 21, 38, 5).strftime('%Y-%m-%dT%H:%M:%S')    
          
}
# print(type(editor_account))
# print(editor_account["editor"]["member_since"])
    
# submit the request
r = requests.post(KERAS_REST_API_URL,json = editor_account).json()

# ensure the request was sucessful
# if r["success"]:
   
print(r)

# otherwise, the request failed
# else:
#     print("Request failed")