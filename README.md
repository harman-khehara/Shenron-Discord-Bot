# Shenron - Discord Bot :robot:

<h2 id="installation">Installation Requirements</h2>

<p>Ensure that you have <code>Python 3</code> or higher installed on your device. Note that <code>Python 3.5.3</code> or higher is required for the discord.py API wrapper.</p>

<ol>
  <li>First, create a Discord Bot account by logging in to the Discord website and then navigating to the <a href="https://discord.com/developers/applications">application</a> page.
  </li>
  <li>Create a new application and then go to the "Bot" tab and click "Add Bot" to create a new bot with default settings. After this has been done, copy the token which you will later have to enter in the Python bot code.
  </li>
  <li>Next, in order to invite your bot to join your Discord Server, go to the "OAuth2" tab and under the "scopes" section, check the box next to "Bot". Under the "permissions" section, give the bot the following permissions: 
    <ul>
      <li>View Channels</li>
      <li>Manage Channels</li>
      <li>Manage Roles</li>
      <li>Manage Emojis</li>
      <li>View Audit Log</li>
      <li>Manage Webhooks</li>
      <li>Manage Server</li>
      <li>Send Messages</li>
      <li>Embed Links</li>
      <li>Attach Files</li>
      <li>Add Reactions</li>
      <li>Use External Emoji</li>
      <li>Manage Messages</li>
      <li>Read Message History</li>
      <li>Manage Messages</li>
      <li>Mention Everyone</li>
    </ul>  
  </li>
  <li>After adding the necessary permissions, click the "copy" button above the "permissions" section and paste this link into a web browser. This will allow you to connect your bot to your Discord server. Note that your Discord account will need "Manage Server" permissions in order to add your bot to your Discord server.
  </li>
</ol>

<p>Now you will need to install the discord.py API wrapper for Python in order to run the code for the bot.</p>
<ul>
  <li>For macOS/Linux, use the following command: <code>python3 -m pip install -U discord.py</code></li>
  <li>For Windows, use the following command: <code>py -3 -m pip install -U discord.py</code></li>
</ul>

<p>Next, <code>git clone</code> this repostiory.</code></p>
<ul>
  <li>If you are going to use a <code>.env</code> file to store your token, make sure the <code>.env</code> file is stored in the same directory as the <code>main.py</code> file.
  </li>
  <li>If you are using a <code>.env</code> file, install the <code>Python-dotenv</code> package using the following command: <code>pip install python-dotenv</code>. Note that <code>Python 3.4</code> or higher already comes with an installation of the pip package installer.
  </li>
  <li>Open the </code>main.py</code> file and enter the token you previously copied where it says 'TOKEN':
  </li>
</ul>


 


  
  
