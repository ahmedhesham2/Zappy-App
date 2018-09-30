import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { Zappy1Component } from './zappy1.component';

describe('Zappy1Component', () => {
  let component: Zappy1Component;
  let fixture: ComponentFixture<Zappy1Component>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ Zappy1Component ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(Zappy1Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
