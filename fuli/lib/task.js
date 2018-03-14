const log = require('./log');
class Task {
    constructor(props){
        this.retry = 0;
        this.job = props.job;
        this.job_promise = null;
        this.status = 'ready';
    }
    async start(){
        let value;
        this.status = 'padding';
        try{
            this.job_promise = this.job();
            value = await this.job_promise;
            this.status = 'over';
        }catch(e){
            log(e);
            if(this.retry < 3)
                this.retry = this.retry+1;
            else
                this.props.error?this.props.error():null;
        }
        return value;
    }
    async end(){
        this.status === 'padding'?this.job_promise.reject():null;
    }
}

module.exports = Task;