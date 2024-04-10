import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EvaluationEnseignementComponent } from './evaluation-enseignement.component';

describe('EvaluationEnseignementComponent', () => {
  let component: EvaluationEnseignementComponent;
  let fixture: ComponentFixture<EvaluationEnseignementComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EvaluationEnseignementComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EvaluationEnseignementComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
