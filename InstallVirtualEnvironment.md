## First UV install kia ya zada fast hay pip say ya bhi packages install kay liay use hota hay ager pip say virtual Environment banana hay TODO

1st way - by pip (pip -m venv .venv) => venv virtual Env hay aur .venv (folder name hay)

## To activate The environment

(.venv\Scripts\activate -> run this )

2nd way - by uv

1st install UV (pip install uv)
2nd uv venv (done virtual environment ban gaya )

(To activate The environment )
 (.venv\Scripts\activate -> run this )

Install Django
ham nay UV say banaya hay virtual environment to ab hamin kuch bhi install karna hay to ya karna ho ga

uv pip packgage name -> to insatll packages by UV using this method in virtual environment

## (So For Download django )

(uv pip install Django ->Done )

(Django ko use kar kay ham project banain gay )

(django-admin startproject projectname -> ais command say bany ga project )

cd djangoProject -> say project kay folder may a jain gay

python manage.py runserver -> run server ho ga ya karny say

Sath may ak file bhi ban jay gi db.sqlite3 (database name) hota hay ya

ham yaha port bhi day sakty hain hay default port 8000 hota hay lakin ais port pay kuch run ho raha hay to phir ham apna port bhi day sakty hain

(python manage.py runserver 80001) -> 80001 port bhi day sakty hain

## To make Apps in django use this command

(python .\manage.py startapp fristApp) ->ya use hoti hay app vali files banany kay liay ya kuch extra install nahi karta hay

## After app was made

(1. 1st approach: hamin app may hi views milta hay to apps bananay kay liay sab say phalay ham template folder banin gay aur aus may same app kay name ka folder bany ga jis may html files ati hain)

   2nd approach: ya hay kay ham same template valy project may jo folder hay ausi may ak folder app kay name ka banin aur aus may sari app ki html files dal day jo dil karay vo karo

## Rendering html files of app

hamary pass views.py app may bhi hota hay to same ak function bano apny route kay name ka aur phir aus ko same render kara do

## Url file

to app may to url file hoti hi nahi hay to kia karin main project say url.py same copy and past in your app

## Tailwind setup in django

## (https://chaicode.com/blogs/how-to-add-tailwind-to-your-django-project-and-django-admin)

this is the  link of setup of tailwind css in django

## Pip Insatll in our virtual Environment

ya install karna par raha hay pip Q kay UV say tailwind ko install nahi kar sakty to pip ko bhi virtual environment may install karna ho ga

For install Pip in virtual environment the command is:
**(python -m ensurepip --upgrade) OR (python -m pip install --upgrade pip)**

## Install Tailwind command after pip install

(pip install 'django-tailwind[reload]')
this is the command for install djando with auto reload

(**setting.py may ja kay tailwind likho**)

## To activate Tailwind

python manage.py tailwind init -> run this kuch packages install hon gay phir theme ka name puchin gay

## Theme folder a jay ga

aus ko bhi phir setting.py may install_Apps may likho

## Telling setting.py the name of tailwind app & IPS

yaha hamin apni tailwind app ka name dana hota hay aur sath may internal IPS dani hoti hay Q kay ab ham servers cahlin gay

TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = [
    "127.0.0.1",
]

## Give BIN PATH

NPM_BIN_PATH = "C://Program Files//nodejs//npm.cmd"
(ais path ko lanay kay liay kisi bhi command prompt may likho) -> **where npm**

ya path dia jata hay hamin tailwind install krny say phalay then install karin tailwind ko
**(python manage.py tailwind install)**

## Tailwind Server Start

python manage.py tailwind start

## First Error resolve that comes everytime when you run django server

(You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.) => This error To Solve this use this command
**(python manage.py migrate)**

NOTE: ab hamary pass /admin route kam karny lag jay ga

## Create Super User

(python manage.py createsuperuser) -> ais command kay bad kuch ya cheezin puchy ga

Username (leave blank to use 'hp'): ahmed
Email address:
Password: ahmed7475@ (ya pass dia hay may nay)
Password (again): ahmed7475@
Superuser created successfully.

