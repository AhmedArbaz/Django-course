## First UV install kia ya zada fast hay pip say ya bhi packages install kay liay use hota hay ager pip say virtual Environment banana hay TODO

                                        1st way - by pip (
pip -m venv .venv  => venv virtual Env hay aur .venv (folder name hay)
                                        )
## To activate The environment

(.venv\Scripts\activate -> run this )

                                        2nd way - by uv
1st install UV (pip install uv)
2nd uv venv (done virtual environment ban gaya )

(To activate The environment )
 (.venv\Scripts\activate -> run this )

                                        Install Django 
ham nay UV say banaya hay virtual environment to ab hamin kuch bhi install karna hay to ya karna ho ga 

uv pip packgage name   -> to insatll packages in virtual environment

(So For Download django )

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