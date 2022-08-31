mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"danilofontanaa@gmail.com\"\n\
" > ~/.streamlit/config.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
[theme]\n\
primaryColor = '#d33682'\n\
backgroundColor = '#002b36'\n\
secondaryBackgroundColor = '#586e75'\n\
textColor = '#fff'\n\
" > ~/.streamlit/config.toml