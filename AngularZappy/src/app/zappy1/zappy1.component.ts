import { Component, OnInit } from '@angular/core';
import {Http} from '@angular/http';
import { Tweet } from './tweet.model';

@Component({
  selector: 'app-zappy1',
  templateUrl: './zappy1.component.html',
  styleUrls: ['./zappy1.component.css']
})

export class Zappy1Component implements OnInit {

  tweetsList: Tweet[] = [];
  constructor(private _http: Http) {}

  ngOnInit() {
    this.gettweets().subscribe(response =>
        JSON.parse(response['_body']).map(tweet => this.tweetsList.push( new Tweet(tweet['text'], tweet['time']))
      )
    );

  }
  gettweets() {
    return this._http.get('/zappy/gettweets');
  }

}
