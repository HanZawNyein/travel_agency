/** @odoo-module **/

import {registry} from "@web/core/registry";
import {Component, onWillStart, useState} from "@odoo/owl";


class TodoList extends Component {
    setup() {
        this.state = useState({
            taskList: [
                {"id": 1, "name": "Sample Task 1", "completed": false},
                {"id": 2, "name": "Sample Task 2", "completed": false},
                {"id": 3, "name": "Sample Task 3", "completed": true},
                {"id": 4, "name": "Sample Task 4", "completed": false},
                {"id": 5, "name": "Sample Task 5", "completed": false},
            ]
        });
        // console.log("i am here.");
        // console.log(this.state.taskList);
        onWillStart(async () => {
            await this.getAllTask();
        })
    }

    async getAllTask() {
        const orm = this.env.services.orm
        // var allTaskList =
        // console.log(allTaskList)
        this.state.taskList = await orm.searchRead("ica.todo", [], ['name', 'completed']);
    }

}

TodoList.template = "ica_todo.TodoList";

registry.category("actions").add("ica_todo.todo_client_action", TodoList);
