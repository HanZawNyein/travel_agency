/** @odoo-module **/

import {registry} from "@web/core/registry";
import {Component, onWillStart, useState} from "@odoo/owl";


class TodoList extends Component {
    setup() {
        this.model = "ica.todo"
        this.orm = this.env.services.orm
        this.state = useState({
            taskList: []
        });
        onWillStart(async () => {
            await this.getAllTask();
        })
    }

    async getAllTask() {
        this.state.taskList = await this.orm.searchRead(this.model, [], ['name', 'completed']);
    }

    async toggleTask(e,task){
        await this.orm.write(this.model,[task.id],{"completed":e.target.checked})
    }

    async deleteTask(task){
        await this.orm.unlink(this.model,[task.id])
        await this.getAllTask()
    }

}

TodoList.template = "ica_todo.TodoList";

registry.category("actions").add("ica_todo.todo_client_action", TodoList);
