---
---
function createMainView() {
    return {
    container:"pubdb_div",
	rows: [
	    {
		view:"template",
		type:"header",template:"Auton Lab Publication Database"
	    },
	    {
	    rows: [{
		    view:"datatable",
		    id:"pubtable",
		    autoheight:true,
			width:0,
			columns:[
				{id:"year",header:["Year",{content:"selectFilter"}],tooltip:false,width:70,sort:"int"},
				{id:"ENTRYTYPE",header:["Type",{content:"selectFilter"}],template:function(obj){return obj.ENTRYTYPE[0].toUpperCase() + obj.ENTRYTYPE.substring(1)},width:120,sort:"string",tooltip:false},
				{id:"title",header:["Title",{content:"textFilter"}],fillspace:true},
				{id:"author",header:["Author",{content:"textFilter"}],fillspace:true,sort:"string"}
		    	],
		    tooltip:true,
		    resizeColumn:true,
		    pager:"pdpager",
			url:"{{ '/data/pubs.json' | relative_url}}",
			on:{
		    	"onItemClick":function(id,e,trg){
				updatePopup(this.getItem(id));
				$$("pubpopup").show();
		    	}
			}
		},
	    pdpager
	    ]
	    }
	]
    }
}
