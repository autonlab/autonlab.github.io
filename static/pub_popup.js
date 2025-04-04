function createPopup() {
    return webix.ui({
	view:"popup",
	id:"pubpopup",
	height:300,
	width:500,
	position:"center",
	body:{
	    id:'pubpopup.body',
	    view:'template',
	    template:"Put Stuff Here"
	}
    })
}

function item2HTML(item) {
    outstr = "";
    for (const [key,value] of Object.entries(item))
    {
	if (key == 'id') {continue;}

	outstr = outstr.concat("<b>");
	outstr = outstr.concat(key);
	outstr = outstr.concat(":</b> ");
	if (key == 'url')
	{
		outstr = outstr.concat('<a href="');
	}
	outstr = outstr.concat(value);
	if (key == 'url')
	{
		outstr = outstr.concat('" target="_blank">');
		outstr = outstr.concat(value);
		outstr = outstr.concat('</a>');
	}
	outstr = outstr.concat("<br/>");
    }
    console.log(outstr);
    return outstr;
}

function updatePopup(item) {
    $$('pubpopup.body').setHTML(item2HTML(item));
}
