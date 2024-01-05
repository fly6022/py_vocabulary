
class Random_words { // 传入参数

    constructor({container, packageSource}) { // 构造函数

        this.container = container, // String
        this.packageSource = packageSource // String

    }

}

window.onload = function selector(){ // 选择器

    packageSource = random_words.packageSource;

        rq = new request(packageSource, null);

        getPackage();

    }

class request { // 预请求

    constructor(requestTarget, subTarget){ // 构造函数

        this.subTarget = subTarget; // 备用目标，当主目标请求失败后请求该目标

        this.requestTarget = requestTarget;

        this.Request = new XMLHttpRequest();

            this.Request.open('GET', requestTarget);

            this.Request.send(null);

    }

}

function getPackage(){

    rq = new request(packageSource, null);

    rq.Request.onload = function() {

        requestData = JSON.parse(rq.Request.responseText);
    
        rnd = Math.floor(Math.random() * requestData.length);

        socket()
    
    }

}

function socket(){ // 临时存储桶 & 传出接口
    
    const text = requestData[rnd].text;

    const voice = requestData[rnd].voice;

    const CHN_means = requestData[rnd].CHN_means;

    Output = "<center>" + "<font size=\"10em\">" + text + "</font>" + "</center>\n" + "<center>" + "<font size=\"5em\">" + voice + "<br>" + CHN_means + "</font>" + "</center>";

        const container = document.getElementsByTagName(random_words.container)[0];
    
        container.innerHTML = Output;

    }