$(document).ready(function(){
        $.getJSON('http://localhost:8000/fetch_all_survey',function(data){
            htm=''
            data.record?.map(item=>{
              var data=JSON.stringify(item)
     //         alert(data.length)
              htm+=`<div style="display: flex; flex-direction: column; margin: 10px;align-items: center; width: 300px; height: 300px; padding: 5px; border: 1px solid #bdc3c7;box-shadow: 2px 2px #ecf0f1;elevation: below;border-radius: 10px;">
           <div style="padding: 5px; display: flex;">
              <div style="font-weight: bolder;width:200px;text-align:left;font-size: 24px;"><center>${item.title}<center></div>
           </div>
           <div style="width:200px;text-align:left;font-size:15px;padding-top: 14px;"><i>Description: ${item.description}</i></div>
           <div style="width:200px;text-align:left;font-weight: bold;padding-top: 14px;">Starting Date: ${item.sdate}</div>
           <div style="width:200px;text-align:left;font-weight: bold;padding-top: 14px;">Ending date: ${item.edate} </div>
           <div style="margin-top: 15px;"><a href='http://localhost:8000/displaysurvey?record=${data}' style="text-decoration: none;color: black;"><button style="width: 130px;;height: 40px;background-color: #FF6864;color:#0B4141;border-radius: 5px;font-weight: bold;cursor: pointer;">Give Survey</button></a></div>
     
           </div>`
          })
            $('#surveylist').html(htm)
          })
     
     
    } )