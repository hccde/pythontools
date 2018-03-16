const log = require('./log');
import const_para = require('../config/const');
let id = 0;

const _task_pool = {

}

class Task {
    constructor(props){
        this.retry = 0;
        this.job = props.job;
        this.job_promise = null;
        this.id = id++;
        this._status = const_para.READY;
        // this.status = const_para.READY;
    }

    set status(s){
        this._status = s;
        if(s === const_para.REJECTED || s === const_para.FULFILLED){

        }
    }

    get status(){
        return this._status;
    }
    
    async start(){
        let value;
        this.status = const_para.PENDING;
        try{
            this.job_promise = this.job();
            value = await this.job_promise;
            this.status = const_para.FULFILLED;
        }catch(e){
            log(e);
            if(this.retry < 3){
                this.retry = this.retry+1;
                this.status = const_para.PENDING;
                this.start();
            }
            else{
                this.props.error?this.props.error():null;
                this.status = const_para.REJECTED;
            }
        }
        return value;
    }
    async end(){
        this.status === const_para.PENDING?this.job_promise.reject():null;
        this.status = const_para.REJECTED;
    }
}

module.exports = Task;