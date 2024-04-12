import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AffichageEvaluationComponent } from './affichage-evaluation.component';

describe('AffichageEvaluationComponent', () => {
  let component: AffichageEvaluationComponent;
  let fixture: ComponentFixture<AffichageEvaluationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AffichageEvaluationComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AffichageEvaluationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
