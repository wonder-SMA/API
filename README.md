<h1><p align="center">docker-compose-api</p></h1>

Docker-compose for api services for Bitcoin

Works on Docker version 19.03.12

<h1>before build</h1>
<ul>
<li>Open the <b>.env</b> file and write your environment variables</li>
<li>If you want to have a local database, just open <b>docker-compose.yml</b> file and uncomment the line
<b>volumes</b></li>
<li>The local database will be located at <b>./databases/my_db</b></li>
</ul>
<h1>build with docker-compose</h1>
<pre>docker-compose build</pre>

<h1>run services</h1>
<pre>docker-compose up</pre>
<ul>
<li>Open your browser and enter <b>127.0.0.1:5000/last</b> to get the latest data and <b>127.0.0.1:5000/history</b> to get all data</li>
<li>if you have some database connection error, just run the following code:</li>
<pre>docker-compose stop</pre>
<pre>docker-compose start</pre>
</ul>
