function login() {

    let username =
    document.getElementById("username").value;

    let password =
    document.getElementById("password").value;

    if (username === "" || password === "") {
        document.getElementById("message").innerText =
        "Fields cannot be empty";
        return;
    }

    if (username === "admin" &&
        password === "admin123") {
        localStorage.setItem("loggedIn", "true");
        window.location.href =
        "dashboard.html";
    }
    else {
        document.getElementById("message").innerText =
        "Invalid Credentials";
    }
}


function markAttendance() {

    if (localStorage.getItem("attendance") === "marked") {

        document.getElementById("attendanceMessage").innerText =
        "Attendance already marked";
        return;
    }

    localStorage.setItem("attendance", "marked");

    document.getElementById("attendanceMessage").innerText =
    "Attendance marked successfully";
}


function applyLeave() {

    let leaveType =
    document.getElementById("leaveType").value;

    let startDate =
    document.getElementById("startDate").value;

    let endDate =
    document.getElementById("endDate").value;

    let reason =
    document.getElementById("reason").value;

    if(
        startDate === "" ||
        endDate === "" ||
        reason === ""
    ){
        document.getElementById("leaveMessage").innerText =
        "All fields are mandatory";

        return;
    }

    let leaveData = {
        leaveType: leaveType,
        startDate: startDate,
        endDate: endDate,
        reason: reason,
        status: "Pending"
    };

    localStorage.setItem(
        "leaveRequest",
        JSON.stringify(leaveData)
    );

    document.getElementById("leaveMessage").innerText =
    "Leave Request Submitted | Status: Pending";
}


window.addEventListener("load", function () {

    if (window.location.pathname.includes("leave_status.html")) {

        let leaveData =
        JSON.parse(localStorage.getItem("leaveRequest"));

        if (leaveData) {

            document.getElementById("leaveStatus").innerText =
            "Type: " + leaveData.leaveType +
            "\nStart Date: " + leaveData.startDate +
            "\nEnd Date: " + leaveData.endDate +
            "\nReason: " + leaveData.reason +
            "\nStatus: " + leaveData.status;
        }
        else {

            document.getElementById("leaveStatus").innerText =
            "No leave requests found";
        }
    }

});
window.addEventListener("load", function () {

    if (window.location.pathname.includes("admin.html")) {

        let leaveData =
        JSON.parse(localStorage.getItem("leaveRequest"));

        if (leaveData) {

            document.getElementById("leaveDetails").innerText =
            "Type: " + leaveData.leaveType +
            "\nStart Date: " + leaveData.startDate +
            "\nEnd Date: " + leaveData.endDate +
            "\nReason: " + leaveData.reason +
            "\nStatus: " + leaveData.status;
        }
    }
});


function approveLeave() {

    let leaveData =
    JSON.parse(localStorage.getItem("leaveRequest"));

    leaveData.status = "Approved";

    localStorage.setItem(
        "leaveRequest",
        JSON.stringify(leaveData)
    );

    document.getElementById("adminMessage").innerText =
    "Leave Approved Successfully";

    document.getElementById("leaveDetails").innerText =
        "Type: " + leaveData.leaveType +
        "\nStart Date: " + leaveData.startDate +
        "\nEnd Date: " + leaveData.endDate +
        "\nReason: " + leaveData.reason +
        "\nStatus: " + leaveData.status;
}
function logout(){

    localStorage.removeItem("loggedIn");

    window.location.href = "login.html";
}