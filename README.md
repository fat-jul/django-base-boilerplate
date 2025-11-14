# django-base-boilerplate


tailwind & daisy ui installation 

cd..
npm int -y
npm install tailwindcss @tailwindcss/cli
npm i -D daisyui@latest

package.json >> add line :
    "watch:css": "tailwindcss -i  ./project_directory/static/css/src/input.css -o ./project_directory/static/css/src/output.css --watch"

npm run watch:css