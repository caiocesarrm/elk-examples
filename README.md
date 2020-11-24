docker-elk - Contém o Elasticsearch, Logstash e Kibana utilizando docker-compose. 
Para iniciar o elk use o comando: docker-compose -f docker-compose.yml -f extensions/apm-server/apm-server-compose.yml up

elk-django - Contém um serviço REST em django já configurado para enviar para o elasticsearch citado na seção anterior, e um endpoint com os logs prontos

elk-netcore - Mesma coisa do elk-django, servidor web api em .net core configurado para enviar os logs para o elasticsearch

sos_pet_apm_django_example - Servidor web django configurado com APM, o apm pode ser monitorado no kibana.
