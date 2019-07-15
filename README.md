# Powershell Atak Analizi<br>
Used Sysmon Rule Tagging attribute for detecting malicious activity on Powershell by the help of some Mitre Att&ck Matrix techniques. 


# Requirements

ElasticSearch - (6.4.1) <br>
Winlogbeat - (6.4.1)<br>
Logstash - (6.4.1)<br>
Kibana - (6.4.1)<br>
Sysmon - v8+<br>
Powershell - v5+<br>

# Settings Needed

<b>GPO settings</b> <br><br>
Go and type gpedit.msc on Powershell Commandline go Windows Powershell and turn on Module Logging, Powershell Script Block Logging.<br><br>
<b>Configuration Settings</b> <br><br>
Create a powershell filter configuration file for Logstash.<br>
Edit ElasticSearch Winlogbeat and Kibana yaml files for getting datas.

