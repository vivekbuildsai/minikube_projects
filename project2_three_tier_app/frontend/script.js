async function getEmployees() {

    const response = await fetch("/employees");

    const employees = await response.json();

    const employeeList = document.getElementById("employee-list");

    employeeList.innerHTML = "";

    employees.forEach(employee => {

        const li = document.createElement("li");

        li.textContent = employee.name;

        employeeList.appendChild(li);

    });

}
