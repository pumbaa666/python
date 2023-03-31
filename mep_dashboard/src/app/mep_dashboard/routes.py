from operator import itemgetter
from flask import render_template
from flask_login import login_required
from app.mep_dashboard import app, keys_found, datastore, key_list


@app.route('/')
@app.route('/index')
@login_required
def index():
    all_meps = []
    for key in keys_found:
        key_minus_keyspace = key.decode().rsplit(":", 1)[1]
        ticket_info = datastore.get_hash_by_keys(name=key_minus_keyspace, keys=key_list)
        task = {}
        if ticket_info['CR:parent'] is not None:
            task['TaskId'] = ticket_info['CR:parent']['key']
            task['Summary'] = ticket_info['CR:parent']['fields']['summary']
            task['OwnerFullName'] = ticket_info['CR:parent']['fields']['creator']['displayName']
            task['OwnerShortName'] = ticket_info['CR:parent']['fields']['creator']['name']
            task['DueDate'] = ticket_info['CR:parent']['fields']['duedate']
            task['Status'] = ticket_info['CR:parent']['fields']['status']['name']
        if ticket_info['CR'] is not None:
            task['JiraId'] = ticket_info['CR']['key']
            task['Changes'] = ticket_info['CR']['fields']['customfield_11469']
            task['Env'] = ticket_info['environment'].decode("utf-8")
        if ticket_info['version'] is not None:
            task['Version'] = ticket_info['version'].decode("utf-8")
        if ticket_info['application'] is not None:
            task['ArtifactId'] = ticket_info['application'].decode("utf-8")
        if ticket_info['DMDB'] is not None:
            task['AppRisk'] = ticket_info['DMDB']['risk']
            task['AppImpact'] = ticket_info['DMDB']['impact']
            task['AppScope'] = ticket_info['DMDB']['scope']
            task['AppType'] = ticket_info['DMDB']['apptype']
            task['AppExtension'] = ticket_info['DMDB']['extension']
            task['AppDescription'] = ticket_info['DMDB']['description']
        all_meps.append(task)
    all_meps = sorted(all_meps, key=itemgetter('TaskId'))
    return render_template("index.html", all_meps=all_meps)


@app.route('/mep_list/<env>')
@login_required
def mep_list(env):
    mep_list = []
    for key in keys_found:
        key_minus_keyspace = key.decode().rsplit(":", 1)[1]
        ticket_info = datastore.get_hash_by_keys(name=key_minus_keyspace, keys=key_list)
        print(ticket_info['environment'].decode("utf-8"))
        task = {}
        if ticket_info['CR:parent'] is not None:
            task['TaskId'] = ticket_info['CR:parent']['key']
            task['Summary'] = ticket_info['CR:parent']['fields']['summary']
            task['OwnerFullName'] = ticket_info['CR:parent']['fields']['creator']['displayName']
            task['OwnerShortName'] = ticket_info['CR:parent']['fields']['creator']['name']
            task['DueDate'] = ticket_info['CR:parent']['fields']['duedate']
            task['Status'] = ticket_info['CR:parent']['fields']['status']['name']
        if ticket_info['CR'] is not None:
            task['JiraId'] = ticket_info['CR']['key']
            task['Changes'] = ticket_info['CR']['fields']['customfield_11469']
            task['Env'] = ticket_info['CR']['fields']["customfield_11966"]["value"]
        if ticket_info['version'] is not None:
            task['Version'] = ticket_info['version'].decode("utf-8")
        if ticket_info['application'] is not None:
            task['ArtifactId'] = ticket_info['application'].decode("utf-8")
        if ticket_info['DMDB'] is not None:
            task['AppRisk'] = ticket_info['DMDB']['risk']
            task['AppImpact'] = ticket_info['DMDB']['impact']
            task['AppScope'] = ticket_info['DMDB']['scope']
            task['AppType'] = ticket_info['DMDB']['apptype']
            task['AppExtension'] = ticket_info['DMDB']['extension']
            task['AppDescription'] = ticket_info['DMDB']['description']
        if ticket_info['environment'].decode("utf-8") == env:
            mep_list.append(task)
    mep_list = sorted(mep_list, key=itemgetter('TaskId'))
    return render_template("mep_list.html", mep_list=mep_list)


@app.route('/deploy_list/<env>')
@login_required
def deploy_list(env):
    list_deploy = []
    for key in keys_found:
        key_minus_keyspace = key.decode().rsplit(":", 1)[1]
        ticket_info = datastore.get_hash_by_keys(name=key_minus_keyspace, keys=key_list)
        print(ticket_info['environment'].decode("utf-8"))
        task = {}
        if ticket_info['CR:parent'] is not None:
            task['TaskId'] = ticket_info['CR:parent']['key']
            task['OwnerFullName'] = ticket_info['CR:parent']['fields']['creator']['displayName']
            task['DueDate'] = ticket_info['CR:parent']['fields']['duedate']
            task['Status'] = ticket_info['CR:parent']['fields']['status']['name']
            if ticket_info['CR:parent']['fields']['customfield_11762'] is not None:
                task['ITC'] = str('Yes')
            if ticket_info['CR:parent']['fields']['customfield_14188'] is not None:
                task['ITC_todo'] = ticket_info['CR:parent']['fields']['customfield_14188']
            if ticket_info['CR:parent']['fields']['customfield_14165'] is not None:
                task['validation'] = ticket_info['CR:parent']['fields']['customfield_14165']['value']
        if ticket_info['CR'] is not None:
            task['JiraId'] = ticket_info['CR']['key']
            task['Env'] = ticket_info['CR']['fields']["customfield_11966"]["value"]
        if ticket_info['version'] is not None:
            task['Version'] = ticket_info['version'].decode("utf-8")
        if ticket_info['application'] is not None:
            task['ArtifactId'] = ticket_info['application'].decode("utf-8")
        if ticket_info['CR'] is not None and ticket_info['application'] is not None:
            task['Servers'] = ''
        if ticket_info['DMDB'] is not None:
            task['AppType'] = ticket_info['DMDB']['apptype']
            task['AppExtension'] = ticket_info['DMDB']['extension']
        if ticket_info['environment'].decode("utf-8") == env:
            list_deploy.append(task)
    list_deploy = sorted(list_deploy, key=itemgetter('TaskId'))
    return render_template("deploy_list.html", list_deploy=list_deploy)
