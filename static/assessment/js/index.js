window.addEventListener('load', function () {
    document.getElementById('accordion2button').click();
    document.getElementById('accordion3button').click();
});

function calculateRealistic() {
    let total = 0;
    id = ['HCRAY1', 'HCRAY2', 'HCRAY3', 'HCRCY1', 'HCRCY2', 'HCRCY3', 'HCRLT1', 'HCRLT2', 'HCRLT3']
    for (item in id) {
        if (document.getElementById(id[item]).checked) total++;
    }
    return total;
}

function calculateInvestigative() {
    let total = 0;
    id = ['HCIAY1', 'HCIAY2', 'HCIAY3', 'HCICY1', 'HCICY2', 'HCICY3', 'HCILT1', 'HCILT2', 'HCILT3']
    for (item in id) {
        if (document.getElementById(id[item]).checked) total++;
    }
    return total;
}

function calculateArtistic() {
    let total = 0;
    id = ['HCAAY1', 'HCAAY2', 'HCAAY3', 'HCACY1', 'HCACY2', 'HCACY3', 'HCALT1', 'HCALT2', 'HCALT3']
    for (item in id) {
        if (document.getElementById(id[item]).checked) total++;
    }
    return total;
}

function calculateSocial() {
    let total = 0;
    id = ['HCSAY1', 'HCSAY2', 'HCSAY3', 'HCSCY1', 'HCSCY2', 'HCSCY3', 'HCSLT1', 'HCSLT2', 'HCSLT3']
    for (item in id) {
        if (document.getElementById(id[item]).checked) total++;
    }
    return total;
}

function calculateEnterprising() {
    let total = 0;
    id = ['HCEAY1', 'HCEAY2', 'HCEAY3', 'HCECY1', 'HCECY2', 'HCECY3', 'HCELT1', 'HCELT2', 'HCELT3']
    for (item in id) {
        if (document.getElementById(id[item]).checked) total++;
    }
    return total;
}

function calculateConventional() {
    let total = 0;
    id = ['HCCAY1', 'HCCAY2', 'HCCAY3', 'HCCCY1', 'HCCCY2', 'HCCCY3', 'HCCLT1', 'HCCLT2', 'HCCLT3']
    for (item in id) {
        if (document.getElementById(id[item]).checked) total++;
    }
    return total;
}

function calculateHollandCode() {
    let HollandCode = [];

    let Realistic = calculateRealistic();
    let Investigative = calculateInvestigative();
    let Artisitic = calculateArtistic();
    let Social = calculateSocial();
    let Enterprising = calculateEnterprising();
    let Conventional = calculateConventional();

    let values = { Realistic, Investigative, Artisitic, Social, Enterprising, Conventional };
    let sorted = Object.entries(values).sort(([, a], [, b]) => b - a);

    HollandCode.push(sorted[0][0], sorted[1][0], sorted[2][0]);

    return HollandCode;
}

// This function retrieves the value of a cookie by name
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    return parts.length === 2 ? parts.pop().split(';').shift() : null;
}

function sendData() {
    const submitBtn = document.getElementById("Btn");
    submitBtn.innerHTML = `<span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>Sending...`;
    submitBtn.disabled = true;

    let _name = document.getElementById('name').value;
    let _age = document.getElementById('age').value;
    let _sex;
    if (document.getElementById('sexRadio1').checked) {
        _sex = document.getElementById('sexRadio1').value;
    } else if (document.getElementById('sexRadio2').checked) {
        _sex = document.getElementById('sexRadio2').value;
    } else {
        alert("Select Sex in general information");
        return;
    }

    let _stream;
    if (document.getElementById('streamRadio1').checked) {
        _stream = document.getElementById('streamRadio1').value;
    } else if (document.getElementById('streamRadio2').checked) {
        _stream = document.getElementById('streamRadio2').value;
    } else if (document.getElementById('streamRadio3').checked) {
        _stream = document.getElementById('streamRadio3').value;
    } else {
        alert("Select Stream in High School Marks");
        return;
    }

    let _subject1_name = document.getElementById('subject1_name').value;
    let _subject1_marks = document.getElementById('subject1_marks').value;

    let _subject2_name = document.getElementById('subject2_name').value;
    let _subject2_marks = document.getElementById('subject2_marks').value;

    let _subject3_name = document.getElementById('subject3_name').value;
    let _subject3_marks = document.getElementById('subject3_marks').value;

    let _subject4_name = document.getElementById('subject4_name').value;
    let _subject4_marks = document.getElementById('subject4_marks').value;

    let _subject5_name = document.getElementById('subject5_name').value;
    let _subject5_marks = document.getElementById('subject5_marks').value;

    let _HC = calculateHollandCode();

    var csrftoken = getCookie('csrftoken');

    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 302) {
            var json = JSON.parse(this.responseText);
            console.log(json.url);
            window.location.href = json.url;
        }
    };
    xhr.open("POST", "/assessment/", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.setRequestHeader('X-CSRFToken', csrftoken);
    xhr.onload = function () {
        console.log(xhr.responseText);
    };
    xhr.send("name=" + _name + "&age=" + _age + "&sex=" + _sex + "&stream=" + _stream + "&subject_1_name=" + _subject1_name + "&subject_1_marks=" + _subject1_marks + "&subject_2_name=" + _subject2_name + "&subject_2_marks=" + _subject2_marks + "&subject_3_name=" + _subject3_name + "&subject_3_marks=" + _subject3_marks + "&subject_4_name=" + _subject4_name + "&subject_4_marks=" + _subject4_marks + "&subject_5_name=" + _subject5_name + "&subject_5_marks=" + _subject5_marks + "&hollandCode1=" + _HC[0] + "&hollandCode2=" + _HC[1] + "&hollandCode3=" + _HC[2]);
}