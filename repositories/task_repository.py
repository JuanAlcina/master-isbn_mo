from models.task import Task, db

class TaskRepository:
    @staticmethod
    def create_task(name, description):
        task = Task(name=name, description=description)
        db.session.add(task)
        db.session.commit()
        return task
    @staticmethod
    def modify_task(name, description):
        res = Task.query.filter_by(name=name).update(dict(description=description))
        db.session.commit()
        return res
    
    