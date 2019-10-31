import { Component } from '@angular/core';
import { HttpClient} from '@angular/common/http';
import { Observable } from 'rxjs';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  title = 'app';

  constructor(private httpc: HttpClient) {}

  getQuestions():Observable<any>{
            return this.httpc.get("http://0.0.0.0:8000/ewc/questions");
  }

}