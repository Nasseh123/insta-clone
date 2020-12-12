function commentsKil(){
    var commentsKills=document.querySelectorAll("#comentsKill");
    for(i=0;i<commentsKills.length;i++){   
        commentsKills[i].remove()
    }
}