server{
    server_name support.axas.ru;

    location / {
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_set_header X-NginX-Proxy true;
        proxy_pass http://localhost:81;
    }



    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/support.axas.ru/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/support.axas.ru/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

}

server{
    if ($host = support.axas.ru) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


    server_name support.axas.ru;
    listen 80;
    return 404; # managed by Certbot


}