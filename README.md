# Shenron - Discord Bot :robot:

<p>Shenron is a Discord Bot designed to interact with users on Discord by answering commands and questions relating to the popular <a href="https://en.wikipedia.org/wiki/Dragon_Ball">Dragon Ball franchise</a>. In the Dragon Ball series, Shenron is a magical wish-granting dragon. The name of this Discord Bot comes from Shenron's ability to answer questions pertaining to almost anything within the Dragon Ball universe. The Shenron Discord Bot allows users to perform various actions within Discord such as adding or removing roles, in addition to allowing users to make use of additional Dragon Ball themed commands.</p>

<h2 id="installation">Installation Requirements</h2>

<p>Ensure that you have <code>Python 3</code> or higher installed on your device. Note that <code>Python 3.5.3</code> or higher is required for the discord.py API wrapper. Additionally, ensure you have added Python to your PATH variable on your operating system to be able to use Python commands in the terminal.</p>

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

<ol>
  <li>If you plan to use a <code>.env</code> to store the token for the bot, follow the steps listed under (1.).
    <ul>
      <li>If you are going to use a <code>.env</code> file to store your token, make sure the <code>.env</code> file is stored in the same directory as the <code>main.py</code>  file.
      </li>
      <li>If you are using a <code>.env</code> file, install the <code>Python-dotenv</code> package using the following command: <code>pip install python-dotenv</code>. Note that <code>Python 3.4</code> or higher already comes with an installation of the pip package installer.
      </li>
      <li>Open the </code>main.py</code> file and enter the token you previously copied where it says 'TOKEN':
      </li>
    </ul>
  </li>

  <li>If you don't plan to use a <code>.env</code> file to store your token, follow the steps listed under (2.).
    <ul>
      <li>Remove the following lines of code from <code>main.py</code> which include support for the use of a <code>.env</code> file:
      </li>
    </ul>
      
     
      ...
    
      from dotenv import load_dotenv # Remove this line
      
      ...
      
      load_dotenv() # Remove this line
      
      ... 
      
      client.run(os.getenv('TOKEN')) # Change this line to --> client.run('TOKEN') # <-- Enter your token where it says TOKEN
      
      ...
      
  </li>
</ol>

<p>Now use the <code>cd</code> command on Command Prompt for Windows or Terminal for macOS/Linux to change the current directory to the location of the <code>main.py</code> file.</p>
<p>Use the following command to run <code>main.py</code> on Windows: <code>py -3 main.py</code></p>
<p>Use the following command to run <code>main.py</code> on macOS/Linux: <code>python3 main.py</code></p>

</p>When the above commands are complete, you should see "Successfully logged in as <code>YOUR_BOT_USERNAME#XXXX</code>" which indicates that your bot is ready to be used.</p>



 


  
  
